def all_left_truncatable_prime(num_tuple):
    x = num_tuple[31]

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatableprime(n):
        if all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))):
            return True
        return False
    res = []
    for i in range(x):
        if is_left_truncatableprime(i):
            res.append(i)
    return sorted(res, reverse=True)