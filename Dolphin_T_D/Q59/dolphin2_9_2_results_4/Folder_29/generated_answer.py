def all_left_truncatable_prime(t):
    x = t[55]

    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        else:
            return False

    def is_truncatable(n):
        if is_prime(n):
            for i in n.split(''):
                if i == '0':
                    return False
                if i:
                    m = n.replace(i, '')
                    return is_prime(m)
        return False

    def all_left_truncatable(x):
        res = []
        for n in range(2, x):
            if is_truncatable(str(n)):
                res.append(n)
        return sorted(res, reverse=True)
    return all_left_truncatable(x)