from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[1]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp != 0:
                temp //= 10
                digit = temp % 10
                if not is_prime(num // 10 ** digit):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)