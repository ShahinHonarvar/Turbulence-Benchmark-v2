def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for k in range(1, len(str_n)):
            if not (is_prime(int(str_n[k:])) and is_prime(int(str_n[:-k]))):
                return False
        return True
    x = numbers[55]
    truncatable_primes = sorted([num for num in range(10, x + 1) if is_prime(num) and is_truncatable_prime(num)])
    return truncatable_primes