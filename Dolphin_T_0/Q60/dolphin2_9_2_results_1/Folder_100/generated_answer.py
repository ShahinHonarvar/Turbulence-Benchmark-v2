def all_left_right_truncatable_prime(i):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x, res = (i[26], [])
    for n in range(2, x + 1):
        if '0' not in str(n) and is_prime(n):
            n, i = (int(str(n)[1:-1]), 0)
            if len(str(n)) == 0:
                n = 0
            while is_prime(n) and n != 0:
                n, i = (int(str(n)[1:-1]), i + 1)
            if i == len(str(n)) - 1:
                res.append(n)
    return sorted(res)