import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(data):
    x = data[84]
    primes = [i for i in range(x - 1, 0, -1) if is_prime(i)]
    self_trunc = [i for i in primes if all((is_prime(int(str(i)[j:])) for j in range(len(str(i)) - 1)))]
    return self_trunc[::-1]