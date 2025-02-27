from math import log, sqrt

def all_left_truncatable_prime(a):
    a = list(a)
    ans = []
    for i in range(a[91]):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            i = str(i)
            if '0' not in i:
                t = [int(i[x:]) for x in range(len(i))]
                if all((d % j for d in t)):
                    ans.append(int(i))
    return sorted(ans)