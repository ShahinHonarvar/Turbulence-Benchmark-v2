def all_right_truncatable_prime(tup):
    x = tup[78]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    str_num = str(num)
    for i in range(1, len(str_num)):
        truncatable_num = int(str_num[:-i])
        if not is_prime(truncatable_num):
            return False
    return True