import math

def isprime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def lefttruncatableprime(x):
    result = []
    for i in x:
        str_i = str(i)
        if '0' not in str_i and str_i[0] not in '024568' and isprime(int(str_i)):
            result.append((str_i, i))
    return sorted(result, key=lambda k: k[1], reverse=True)