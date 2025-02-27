def all_left_right_truncatable_prime(numbers):
    x = numbers[52]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        length = len(s)
        for i in range(length):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:length - i])):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_prime(n) and left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)