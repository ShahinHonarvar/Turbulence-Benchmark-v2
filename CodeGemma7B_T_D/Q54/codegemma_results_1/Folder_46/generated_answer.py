def all_right_truncatable_prime(x):
    return sorted([i for i in range(2, x) if SieveOfEratosthenes(i) and is_right_truncatable(i)])

def SieveOfEratosthenes(x):
    prime = [True] * x
    p = 2
    while p * p <= x:
        if prime[p]:
            for i in range(p * 2, x + 1, p):
                prime[i] = False
        p += 1
    return prime[x]

def is_right_truncatable(x):
    if not x:
        return False
    str_x = str(x)
    for i in range(1, len(str_x)):
        if not SieveOfEratosthenes(int(str_x[:-i])):
            return False
    return True