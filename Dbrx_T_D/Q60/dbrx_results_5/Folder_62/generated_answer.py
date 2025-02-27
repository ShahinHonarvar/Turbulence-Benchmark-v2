from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(bound_tuple):
    x = sorted(list(set(bound_tuple)))[70]
    lr_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        num_str = str(num)
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i:i + 3])):
                break
            num_str = num_str[1:] + num_str[len(num_str) - 1]
        else:
            if is_prime(int(num_str)):
                lr_primes.append(num)
    return sorted(lr_primes)