def all_right_truncatable_prime(tup):
    x = tup[50]
    res = []
    for i in range(2, x):
        if is_prime(i):
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[:-j])):
                    break
            else:
                res.append(i)
    res.sort(reverse=True)
    return res

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True