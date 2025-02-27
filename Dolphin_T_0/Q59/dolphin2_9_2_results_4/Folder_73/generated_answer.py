def all_left_truncatable_prime(t):

    def _is_prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[97]
    primes = [2]
    i = 3
    while i < x:
        if _is_prime(i):
            primes.append(i)
        i += 2
    left_truncatable = []
    for prime in primes:
        str_prime = str(prime)
        if all((_is_prime(int(str_prime[index:])) for index in range(len(str_prime)))):
            left_truncatable.append(prime)
    return sorted(left_truncatable)