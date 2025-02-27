def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[36]
    primes = [i for i in range(x) if is_prime(i)]
    left_truncatables = []
    for prime in primes:
        if str(prime)[0] != '0':
            left_truncatable = True
            for digit in str(prime)[1:]:
                if not is_prime(int(digit)):
                    left_truncatable = False
            if left_truncatable:
                left_truncatables.append(prime)
    left_truncatables.sort()
    return left_truncatables