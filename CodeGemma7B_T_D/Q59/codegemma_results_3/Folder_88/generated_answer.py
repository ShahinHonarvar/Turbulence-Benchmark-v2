import math 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):
    primes = []
    for num in range(2, x):
        if num % 10 == 0:
            continue
        if is_prime(num):
            left_truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(num)
    return sorted(primes)