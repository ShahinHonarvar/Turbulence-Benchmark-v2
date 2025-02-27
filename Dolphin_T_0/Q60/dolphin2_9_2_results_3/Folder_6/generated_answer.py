def all_left_right_truncatable_prime(numbers):

    def _is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[74]
    primes = [i for i in range(2, x + 1) if _is_prime(i) and '0' not in str(i)]
    trim_primes = []
    for prime in primes:
        if len(str(prime)) <= 2 or (_is_prime(int(str(prime)[1:-1])) and _is_prime(int(str(prime)[:-1])) and _is_prime(int(str(prime)[1:]))):
            trim_primes.append(prime)
    trim_primes.sort()
    return trim_primes