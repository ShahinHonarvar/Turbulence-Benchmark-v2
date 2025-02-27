def all_left_right_truncatable_prime(tuple_):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_[37]
    primes = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if not is_prime(i):
            continue
        while len(str(i)) > 2:
            i = i // 10
            if not is_prime(i):
                break
        else:
            primes.append(i)
    return sorted(primes, reverse=True)