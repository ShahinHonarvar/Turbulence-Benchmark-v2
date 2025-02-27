from math import sqrt

def righttruncatable_prime(n):
    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits) - 1):
        n = int(''.join(map(str, digits[:-(i + 1)])))
        if not is_prime(n):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    plist = []
    for n in range(1, x):
        if righttruncatable_prime(n):
            plist.append(n)
    return sorted(plist)