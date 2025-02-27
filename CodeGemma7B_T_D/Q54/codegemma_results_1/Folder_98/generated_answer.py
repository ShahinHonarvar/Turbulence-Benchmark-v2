from functools import reduce

def is_prime(x):

    def f(x, i):
        return x % i != 0 and f(x, i - 1) if x > 1 and i > 2 else x == 2
    return f(x, x // 2)

def all_right_truncatable_prime(args):
    x = args[8]
    ls = [i for i in range(2000000) if is_prime(i)]
    res = sorted([i for i in ls if x % i == 0 and is_prime(reduce(lambda a, b: a + b, [int(d) for d in str(i)[::-1]]))], reverse=True)
    return res if res else []