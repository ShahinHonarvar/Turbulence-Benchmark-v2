def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[645]
    rs = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 1:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 1:
                    rs.append(num)
    return sorted(rs) if rs else []