def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n == 0:
            return True
        n2 = int(n / 10)
        return is_right_truncatable_prime(n2)
    x = numbers[87]
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i)])