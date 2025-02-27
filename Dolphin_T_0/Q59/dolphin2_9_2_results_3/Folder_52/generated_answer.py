def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    l = list(t)
    x = l[52]
    trunc_primes = []
    for num in range(x - 1, 1, -1):
        num_str = str(num)
        while num_str and is_prime(int(num_str)):
            trunc_primes.append(int(num_str))
            num_str = num_str[1:]
    return sorted(list(set(trunc_primes)), reverse=True)