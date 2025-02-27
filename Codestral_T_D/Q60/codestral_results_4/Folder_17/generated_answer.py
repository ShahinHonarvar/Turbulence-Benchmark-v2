def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not (int(str(n)[i:]) in primes and int(str(n)[:-i]) in primes):
                return False
        return True
    x = t[36]
    primes = set()
    result = []
    for possiblePrime in range(2, x + 1):
        if all((possiblePrime % j != 0 for j in range(2, int(possiblePrime ** 0.5) + 1))):
            primes.add(possiblePrime)
            if is_truncatable_prime(possiblePrime):
                result.append(possiblePrime)
    return sorted(result, reverse=True)