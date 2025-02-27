def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[39]
    result = []
    for n in range(x, 0, -1):
        if is_prime(n):
            trunc_n = n
            while trunc_n > 9 and is_prime(trunc_n):
                trunc_n //= 10
            if trunc_n == 1 or trunc_n == 2:
                result.append(n)
    return result