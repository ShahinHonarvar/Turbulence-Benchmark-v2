from itertools import count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(x):
    ltp = set()
    for i in count(1):
        if not str(i)[0] == '0':
            num = i
            while num > 0:
                if num not in ltp and is_prime(num):
                    ltp.add(num)
                num = num // 10
        if i > x:
            break
    return sorted(ltp)