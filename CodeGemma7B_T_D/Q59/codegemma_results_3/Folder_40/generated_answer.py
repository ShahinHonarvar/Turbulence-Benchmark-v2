from functools import reduce
from itertools import count

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_zero_integers(n):

    def helper(k):
        s = str(k)
        if '0' not in s:
            yield k
        for i in range(len(s) - 1):
            k = 10 * (k % 10) + k // 10
            if '0' not in str(k):
                yield k
    return helper(n)

def all_left_truncatable_prime(tup):
    x = tup[10]
    allowed_numbers = filter(lambda n: '0' not in str(n), count(x - 1))
    return sorted([n for n in allowed_numbers if is_prime(n)], reverse=True)