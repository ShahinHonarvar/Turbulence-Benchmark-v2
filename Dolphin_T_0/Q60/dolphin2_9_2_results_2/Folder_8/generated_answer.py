def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        while len(str(n)) > 1:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        if not is_prime(n):
            return False
        return True
    x = numbers[41]
    primes = []
    for n in range(x, 1, -1):
        if is_truncatable_prime(n):
            primes.append(n)
    return primes