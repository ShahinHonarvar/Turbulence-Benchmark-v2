def all_left_truncatable_prime(t):
    x = t[992]
    a = []
    i = 2
    while i < x:
        j = i
        flag = True
        while j > 0:
            if j % 2 == 0 or not j % 5 == 0 or j % 10 == 0:
                flag = False
                break
            j //= 10
        j = i
        while j > 0:
            if isprime(j):
                j -= 1
            else:
                flag = False
                break
        if flag:
            a.append(i)
        i += 1
    return sorted(a)

def isprime(i):
    if i % 2 == 0:
        return False
    if i < 2:
        return False
    if i == 2:
        return True
    for j in range(3, i, 2):
        if i % j == 0:
            return False
    return True