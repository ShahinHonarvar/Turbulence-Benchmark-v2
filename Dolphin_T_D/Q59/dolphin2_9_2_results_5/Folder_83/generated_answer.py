def is_truncatable_prime(n):

    def is_prime(p):
        if p < 2:
            return False
        if p == 2 or p == 3:
            return True
        if p % 2 == 0:
            return False
        for i in range(3, int(p ** 0.5) + 1, 2):
            if p % i == 0:
                return False
        return True
    if n < 10:
        return is_prime(int(str(n)))
    for i in range(len(str(n)) - 1, 0, -1):
        if not is_prime(int(str(n)[i:] + str(n)[i - 1])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[24]
    primes = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(primes)