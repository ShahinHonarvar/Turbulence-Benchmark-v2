import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(integers):
    x = integers[1]
    primes = [x - i for i in range(1, x + 1) if is_prime(x - i)]
    right_truncatable_primes = [i for i in primes if all((is_prime(int(str(j))) for j in str(i) if j != 0))]
    return sorted(right_truncatable_primes, reverse=True) or []