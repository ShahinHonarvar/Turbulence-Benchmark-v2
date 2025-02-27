def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    def generate_primes(n):
        return [i for i in range(2, n) if is_prime(i)]

    def filter_left_truncatable(primes):
        return [p for p in primes if left_truncatable(p) and '0' not in str(p)]
    x = numbers[7]
    primes = generate_primes(x)
    left_truncatable_primes = filter_left_truncatable(primes)
    return sorted(left_truncatable_primes)