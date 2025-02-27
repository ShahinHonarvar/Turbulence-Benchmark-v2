def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if n <= 1:
            return False
        for c in str(n)[::-1]:
            n = int(str(n).replace(c, ''))
            if not is_prime(n):
                return False
        return True
    x = t[370]
    ret_list = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            ret_list.append(i)
    ret_list.sort(reverse=True)
    return ret_list if len(ret_list) > 0 else []