def all_right_truncatable_prime(tuple_):

    def is_prime(num):
        if num == 2 or num == 3:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    n, = tuple_
    x = n // 10 ** 91
    primes = []
    for i in range(2, x):
        if is_prime(i):
            if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i))))):
                primes.append(i)
    return sorted(primes)