def all_left_truncatable_prime(t):
    l = []
    for n in t:
        strn = str(n)
        for j in range(1, len(strn)):
            lst = []
            for i in range(j):
                lst.append(strn[i])
            if ltpr(int(''.join(lst))):
                flag = True
            else:
                flag = False
                break
        if flag:
            l.append(n)
    return sorted(l, reverse=True)

def ltpr(n):
    if n == 0 or n == 1 or n == 4 or (n == 6) or (n == 8):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True