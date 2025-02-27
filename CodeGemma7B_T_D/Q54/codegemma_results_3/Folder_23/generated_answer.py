from sympy import S, factorint

def all_right_truncatable_prime(tN):
    left, right = tN
    x = int(tN[77])
    listR = []
    for i in range(left, right - 1):
        l = str(i)
        if S(i).isprime() and S(l[:len(l) - 1]).isprime():
            listR.append(i)
    listR.sort(reverse=True)
    if not listR:
        return []
    return listR