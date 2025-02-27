def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    x = t[20]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatables = []
    for prime in primes:
        trunc = str(prime)
        while len(trunc) > 2:
            if not '0' in trunc and is_prime(int(trunc[1:-1])):
                truncatables.append(prime)
            trunc = str(int(trunc[1:-1]))
    return sorted(list(set(truncatables)), reverse=True)