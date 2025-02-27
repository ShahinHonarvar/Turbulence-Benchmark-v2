def all_left_truncatable_prime(tup):

    def is_left_truncatable_prime(n):
        if n < 2:
            return False
        n_str = str(n)
        return all((is_prime(int(n_str[i:])) for i in range(len(n_str))))

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tup[30]
    result = []
    for i in range(x - 1, 1, -1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result