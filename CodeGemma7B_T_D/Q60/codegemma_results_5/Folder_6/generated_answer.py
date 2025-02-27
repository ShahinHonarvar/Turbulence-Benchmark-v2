def all_left_right_truncatable_prime(value):
    if len(value) != 1 or value[0] <= 0:
        raise ValueError('Input tuple must contain a single positive integer.')
    x = value[0]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            if is_truncatable_prime(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    str_num = str(num)
    n = len(str_num)
    if '0' in str_num:
        return False
    for i in range(1, n):
        truncated_num = int(str_num[i:])
        if not is_prime(truncated_num):
            return False
    for i in range(1, n):
        truncated_num = int(str_num[:-i])
        if not is_prime(truncated_num):
            return False
    return True