def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[71]
    cond = lambda a: all((is_prime(int(str(a)[i:])) for i in range(len(str(a))))) and all((str(a)[i] != str('0') for i in range(len(str(a)))))
    ret_list = []
    for num in range(x, 0, -1):
        if cond(num):
            ret_list.append(num)
    return ret_list