def all_right_truncatable_prime(inputs):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        if n <= 1:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = inputs[14]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i) and is_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes