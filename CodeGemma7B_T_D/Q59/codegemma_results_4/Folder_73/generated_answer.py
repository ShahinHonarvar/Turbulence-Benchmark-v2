import math

def all_left_truncatable_prime(x):
    truncables = []
    for i in range(2, x):
        if isprime(i) and hasnozero(i) and islefttruncatable(i):
            truncables.append(i)
    return sorted(truncables)

def isprime(i):
    if i <= 1:
        return False
    sqrt_i = math.floor(math.sqrt(i))
    for m in range(2, sqrt_i + 1):
        if i % m == 0:
            return False
    return True

def hasnozero(i):
    return not str(i).count('0')

def islefttruncatable(i):
    i_str = str(i)
    for j in range(1, len(i_str)):
        if not isprime(int(i_str[j:])):
            return False
    return True