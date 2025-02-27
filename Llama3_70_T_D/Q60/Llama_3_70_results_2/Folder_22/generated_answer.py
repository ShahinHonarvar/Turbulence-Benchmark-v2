def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        if len(str_n) < 2:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return is_prime(int(str_n))
    x = numbers[85]
    return sorted([n for n in range(11, x + 1) if is_left_right_truncatable_prime(n)])