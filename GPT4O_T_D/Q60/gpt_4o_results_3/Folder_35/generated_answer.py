def all_left_right_truncatable_prime(numbers):
    num = numbers[177]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True

    def valid_prime(n):
        return '0' not in str(n) and is_prime(n)
    primes = [p for p in range(2, num + 1) if valid_prime(p)]
    left_right_truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(left_right_truncatable_primes)