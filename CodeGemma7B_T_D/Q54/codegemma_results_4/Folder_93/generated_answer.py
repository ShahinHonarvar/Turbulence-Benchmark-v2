import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def all_right_truncatable_prime(tp):
    x = tp[11]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)