def all_left_truncatable_prime(p):
    idx = 79
    n = p[idx]
    lst = []
    for i in range(2, n):
        if not str(i).__contains__('0') and is_prime(i) and is_prime(int(str(i)[:-1])):
            lst.append(i)
    lst.sort(reverse=True)
    return lst

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True