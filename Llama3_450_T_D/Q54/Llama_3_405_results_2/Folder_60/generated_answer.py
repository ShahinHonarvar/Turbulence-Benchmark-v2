def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        n = str(n)
        for i in range(len(n), 0, -1):
            if not is_prime(int(n[:i])):
                return False
        return True
    x = numbers[87]
    primes = [i for i in range(2, x) if is_prime(i)]
    truncatable_primes = [i for i in primes if right_truncatable(i)]
    return sorted(truncatable_primes)