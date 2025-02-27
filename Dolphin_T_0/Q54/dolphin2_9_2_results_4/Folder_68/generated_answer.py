def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[1]
    trunc_prime_list = list()
    for i in range(2, x):
        if is_prime(i):
            trunc = i
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                trunc_prime_list.append(i)
    return sorted(trunc_prime_list, reverse=True)