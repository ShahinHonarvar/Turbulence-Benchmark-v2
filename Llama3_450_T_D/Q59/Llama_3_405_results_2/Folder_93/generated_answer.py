def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[11]
    truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable_prime = True
        for i in range(len(num_str)):
            trunc_num_str = num_str[i:]
            if not is_prime(int(trunc_num_str)):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))