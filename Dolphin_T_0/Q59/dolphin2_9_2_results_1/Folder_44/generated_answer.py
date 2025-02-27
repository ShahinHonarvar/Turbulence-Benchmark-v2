def all_left_truncatable_prime(t):
    x = t[39]
    ret_list = []
    for num in range(2, x):
        if all((is_prime(int(str(num)[i:])) for i in range(len(str(num))))):
            ret_list.append(num)
    return sorted(ret_list)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True