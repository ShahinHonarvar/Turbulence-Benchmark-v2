from math import sqrt

def all_left_truncatable_prime(args):
    x = args[29]
    limit = int(sqrt(x))
    res = []
    for i in range(2, x):
        if 0 in str(i):
            continue
        if all((i % j != 0 for j in range(2, limit + 1))):
            j = int(str(i)[1:])
            while j > 1 and all((j % k != 0 for k in range(2, int(sqrt(j)) + 1))):
                res.append(i)
                if len(str(j)) == 1:
                    break
                j = int(str(j)[1:])
    return sorted(res)