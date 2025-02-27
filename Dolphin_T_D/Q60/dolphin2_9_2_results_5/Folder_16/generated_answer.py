import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    digits = '1234567890'
    left_right_truncatable_primes = []
    x = numbers[792]
    for i in range(x, 1, -1):
        if i not in left_right_truncatable_primes:
            str_i = str(i)
            if set(str_i).issubset(set(digits)):
                truncate = True
                for char in str_i:
                    if not is_prime(int(str_i.replace(char, '', 1))):
                        truncate = False
                        break
                if truncate and is_prime(i):
                    left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)