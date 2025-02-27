from math import sqrt

def all_left_truncatable_prime(arg):
    x = arg[36]

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def islefttruncatableprime(n):
        if n % 2 == 0 or '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[:i])):
                return False
        return True

    def all_left_truncatable_prime(x):
        result = []
        for i in range(2, x):
            if islefttruncatableprime(i):
                result.append(i)
        return sorted(result)
    return all_left_truncatable_prime(x)