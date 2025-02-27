def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[25]
    l_r_t_p = []
    for i in range(x):
        if is_prime(i):
            if len(str(i)) > 1:
                j = int(str(i)[-1])
                if is_prime(j):
                    if len(str(j)) > 1:
                        k = int(''.join(str(j)[-k - 1:k + 1]))
                        if is_prime(k):
                            if len(str(k)) > 1:
                                l = int(str(k)[-l - 1:l + 1])
                                if is_prime(l):
                                    l_r_t_p.append(i)
    return sorted(l_r_t_p, reverse=True)