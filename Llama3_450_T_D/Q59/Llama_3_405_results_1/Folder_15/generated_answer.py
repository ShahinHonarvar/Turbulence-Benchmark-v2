def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[6]
    truncatable_primes = []
    for num in range(11, x):
        if '0' in str(num):
            continue
        num_str = str(num)
        all_primes = True
        for i in range(len(num_str)):
            trunc_num = int(num_str[i:])
            if not is_prime(trunc_num):
                all_primes = False
                break
        if all_primes:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)