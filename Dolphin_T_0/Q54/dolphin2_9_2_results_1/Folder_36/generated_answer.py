def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = num_tuple[992]
    res = []
    for i in range(2, num):
        if is_prime(i):
            trunc = i
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                res.append(i)
    return sorted(res)