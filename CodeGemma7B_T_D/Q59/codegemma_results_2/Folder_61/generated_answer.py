def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[3]
    res = []
    for i in range(2, x):
        if isprime(i) and (not str(i).startswith('0')) and all((isprime(int(str(i)[:j])) for j in range(1, len(str(i))))):
            res.append(i)
    return sorted(res, reverse=True)