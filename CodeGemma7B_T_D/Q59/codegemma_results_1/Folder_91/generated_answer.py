from math import sqrt

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    temp = nums[:i]
    if not '0' in temp:
        num = int(''.join(temp))
        if isprime(num):
            ret.append(num)