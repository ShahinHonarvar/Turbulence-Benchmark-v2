def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[30]
    ses = []
    for i in range(2, x + 1):
        if is_prime(i):
            st = str(i)
            if all([is_prime(int(st[1:])) and is_prime(int(st[:-1])) for st in map(str, range(2, i))]):
                ses.append(i)
    return ses