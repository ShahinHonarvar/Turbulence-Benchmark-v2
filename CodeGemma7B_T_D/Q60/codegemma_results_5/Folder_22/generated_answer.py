import math

def all_left_right_truncatable_prime(args):

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        while n >= 10:
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True

    def left_truncatable(n):
        s = str(n)
        for k in range(1, len(s)):
            n = int(s[k:])
            if not isprime(n):
                return False
        return True
    result = []
    if not args:
        limit = int(input('Enter the upper limit: '))
    else:
        limit = max(args)
    for n in range(2, limit + 1):
        if '0' not in str(n) and isprime(n) and right_truncatable(n) and left_truncatable(n):
            result.append(n)
    return sorted(result)