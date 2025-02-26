def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    original_num = str(num)
    while len(original_num) > 0:
        if not is_prime(int(original_num)):
            return False
        original_num = original_num[1:]
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[86]
    left_right_truncatable_primes = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes