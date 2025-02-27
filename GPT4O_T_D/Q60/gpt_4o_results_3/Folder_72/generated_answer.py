def all_left_right_truncatable_prime(numbers):

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

    def is_truncatable_left_right(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or '0' in s or (not is_prime(int(s))):
                return False
        return True

    def is_truncatable_prime(n):
        return '0' not in str(n) and is_prime(n) and is_truncatable_left_right(n)
    x = numbers[31]
    truncatable_primes = []
    for i in range(23, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)