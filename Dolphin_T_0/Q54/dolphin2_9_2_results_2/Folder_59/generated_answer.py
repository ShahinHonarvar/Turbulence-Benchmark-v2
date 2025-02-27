def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        length = len(n)
        for i in range(1, length + 1):
            if not is_prime(int(n[i - 1:])):
                return False
        return True
    x = numbers[84]
    primes = [i for i in range(2, x) if is_truncatable_prime(i) and is_prime(i)]
    return sorted(primes, reverse=True)