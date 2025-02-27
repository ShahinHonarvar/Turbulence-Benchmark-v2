def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2 or any((n % i == 0 for i in range(2, int(n ** 0.5) + 1))):
            return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    x = numbers[73]
    truncatable_primes = [n for n in range(10, x + 1) if is_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)