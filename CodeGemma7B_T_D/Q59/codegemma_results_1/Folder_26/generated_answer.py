import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    prime_set = set()
    for i in range(2, tup[81]):
        if is_prime(i) and '0' not in str(i):
            j = i
            while j >= 10:
                if not is_prime(j):
                    break
                j //= 10
            else:
                prime_set.add(i)
    return sorted(prime_set, reverse=True)