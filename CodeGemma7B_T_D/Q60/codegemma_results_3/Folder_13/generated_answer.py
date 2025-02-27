def all_left_right_truncatable_prime(tup):
    x = tup[784]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            if is_truncatable(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)

def is_prime(num):
    if num <= 1:
        return False
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_truncatable(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    for i in range(1, len(num_str)):
        left_digits = num_str[:i]
        right_digits = num_str[i:]
        left_num = int(left_digits)
        right_num = int(right_digits)
        if not (is_prime(left_num) and is_prime(right_num)):
            return False
    return True