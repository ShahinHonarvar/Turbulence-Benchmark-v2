import math

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[69]
    ltp = []
    for n in range(2, x + 1):
        if isprime(n) and (not '0' in str(n)):
            sn = str(n)
            for k in range(0, len(sn)):
                if not isprime(int(sn[k:])) or (len(sn) - k - 1 > 0 and (not isprime(int(sn[:len(sn) - k - 1])))):
                    break
            else:
                ltp.append(n)
    ltp.sort(reverse=True)
    return ltp