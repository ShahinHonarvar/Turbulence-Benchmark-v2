def all_right_truncatable_prime(x):
    rt_list = []
    for a in range(1, x - 1):
        if is_prime(a):
            rt = a
            for i in range(9, 1, -1):
                b = rt % 10
                if b != i:
                    continue
                rt //= 10
                if not is_prime(rt):
                    break
            else:
                rt_list.append(a)
    rt_list.sort()
    return rt_list

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True