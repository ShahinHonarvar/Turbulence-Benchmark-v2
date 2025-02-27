def all_left_right_truncatable_prime(numbers):
    x = numbers[64]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_truncate = int(str_n[i:])
            right_truncate = int(str_n[:len(str_n) - i])
            if not (is_prime(left_truncate) and is_prime(right_truncate)):
                return False
        return True
    truncatable_primes = [n for n in range(10, x + 1) if is_prime(n) and is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)