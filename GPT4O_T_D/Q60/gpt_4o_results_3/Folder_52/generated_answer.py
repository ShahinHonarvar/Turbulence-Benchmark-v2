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

    def is_left_right_truncatable(prime):
        s = str(prime)
        if '0' in s:
            return False
        while len(s) > 1:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return prime in [2, 3, 5, 7]
    x = numbers[52]
    truncatable_primes = [num for num in range(10, x + 1) if is_prime(num) and is_left_right_truncatable(num)]
    return sorted(truncatable_primes, reverse=True)