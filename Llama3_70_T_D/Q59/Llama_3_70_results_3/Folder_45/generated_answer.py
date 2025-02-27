def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[61]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                truncatable = False
                break
        if truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return left_truncatable_primes