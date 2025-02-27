from math import sqrt

def all_right_truncatable_prime(n):

    def prime(n):
        if n == 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    p = n[975]
    result = []
    for i in range(2, int(sqrt(p)) + 1):
        if prime(i) and p % i == 0:
            f = p
            while f > 0:
                if not prime(f):
                    break
                f //= 10
            else:
                result.append(p)
    return sorted(result, reverse=True) if result else []