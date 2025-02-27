def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[433]
    left_truncatable_primes = []
    for num in range(10, x):
        if '0' in str(num):
            continue
        for i in range(len(str(num))):
            truncated_num = int(str(num)[i:])
            if not is_prime(truncated_num):
                break
        else:
            if is_prime(num):
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)