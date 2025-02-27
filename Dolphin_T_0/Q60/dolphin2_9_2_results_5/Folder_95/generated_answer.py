from math import sqrt

def trim_num(n):
    while n > 9:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[77]
    res = [i for i in range(2, x + 1) if trim_num(i) and is_prime(i)]
    res = [i for i in res if all(is_prime(int('%s' % i))) and all(is_prime(int('%s' % i[::-1]))) and all(is_prime(int('%s' % i[1:]))) and all(is_prime(int('%s' % i[:-1])))]
    return sorted(res)