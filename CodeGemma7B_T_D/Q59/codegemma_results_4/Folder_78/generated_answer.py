def ltp(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(tup):
    x = tup[23]
    res = []
    for n in range(2, x):
        if ltp(n) and (not '0' in str(n)):
            i = 2
            while i != len(str(n)):
                j = int(str(n)[:-i])
                if not ltp(j):
                    break
                i += 1
            else:
                res.append(n)
    return sorted(res)