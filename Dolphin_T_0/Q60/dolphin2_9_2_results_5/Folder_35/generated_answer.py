def all_left_right_truncatable_prime(tpl):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tpl[177]
    ret = []
    for i in range(2, x + 1):
        if is_prime(i) and (not '0' in str(i)):
            trunc = i
            while len(str(trunc)) > 2:
                trunc = int(str(trunc)[1:-1])
                if not is_prime(trunc):
                    break
            else:
                ret.append(i)
    return ret