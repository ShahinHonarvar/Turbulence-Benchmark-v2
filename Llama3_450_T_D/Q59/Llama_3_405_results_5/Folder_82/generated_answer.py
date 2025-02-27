def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[69]
    left_truncatable_primes = set()
    for num in range(10, x):
        if '0' in str(num):
            continue
        all_primes = True
        num_str = str(num)
        for i in range(len(num_str)):
            trunc_num = int(num_str[i:])
            if not is_prime(trunc_num):
                all_primes = False
                break
        if all_primes:
            left_truncatable_primes.add(num)
    return sorted(list(left_truncatable_primes), reverse=True)