def all_right_truncatable_prime(numbers):
    if len(numbers) <= 760:
        return []
    x = numbers[760]

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

    def truncatable_right_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        while len(str_n) > 1:
            str_n = str_n[:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    truncatable_primes = [i for i in range(2, x) if truncatable_right_prime(i)]
    return sorted(truncatable_primes, reverse=True)