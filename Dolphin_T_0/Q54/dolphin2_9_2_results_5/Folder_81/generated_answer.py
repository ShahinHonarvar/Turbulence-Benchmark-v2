import math

def is_prime(num):
    if num in (0, 1):
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(num))
    for i in range(3, 1 + max_div, 2):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc < 10:
                    primes.append(num)
    return sorted(primes)