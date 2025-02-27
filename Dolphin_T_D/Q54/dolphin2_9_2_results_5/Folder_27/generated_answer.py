def all_right_truncatable_prime(numbers):

    def is_prime(nn):
        if nn == 1:
            return False
        for i in range(2, int(nn ** 0.5) + 1):
            if nn % i == 0:
                return False
        return True
    x = numbers[79]
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [i for i in primes if i in primes[::10]]
    return sorted(right_truncatable_primes, reverse=True)