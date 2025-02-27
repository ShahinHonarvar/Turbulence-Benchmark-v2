def all_left_right_truncatable_prime(arr):
    x = arr[14]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        for digit in map(int, str(n)):
            if digit == 0:
                return False
        for i in range(1, len(str(n)) - 1):
            if not is_prime(int(str(n)[i:])):
                return False
            l = len(str(n))
            if not is_prime(int(str(n)[i:l - i])):
                return False
            if i > 1 and (not is_prime(int(str(n)[:i]))):
                return False
            if i > 1 and (not is_prime(int(str(n)[l - i:]))):
                return False
            if not is_prime(int(str(n)[:i]) or int(str(n)[l - i:])):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)])