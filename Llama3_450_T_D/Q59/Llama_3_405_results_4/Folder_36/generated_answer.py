def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[992]
    primes = []
    for i in range(10, x):
        if '0' in str(i):
            continue
        num_str = str(i)
        is_truncatable = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(i)
    return sorted(primes)