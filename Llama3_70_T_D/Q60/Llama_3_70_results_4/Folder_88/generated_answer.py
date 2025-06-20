def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = numbers[93]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable(i) and ('0' not in str(i))]
    return sorted(left_right_truncatable_primes)