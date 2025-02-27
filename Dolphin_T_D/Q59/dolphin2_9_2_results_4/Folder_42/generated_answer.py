def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[64]
    primes = [i for i in range(x) if is_prime(i) and is_left_truncatable(i)]
    return sorted(primes, reverse=True)