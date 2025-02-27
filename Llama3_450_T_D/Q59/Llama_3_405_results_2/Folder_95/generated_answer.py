def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[77]
    truncatable_primes = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                break
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)