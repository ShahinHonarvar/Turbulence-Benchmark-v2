def all_left_right_truncatable_prime(numbers):
    x = numbers[37]

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

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s or not is_prime(n):
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)