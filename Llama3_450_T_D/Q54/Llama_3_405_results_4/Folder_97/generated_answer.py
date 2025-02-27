def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[645]
    right_truncatable_primes = []
    for i in range(2, x):
        num_str = str(i)
        while num_str:
            if not is_prime(int(num_str)):
                break
            num_str = num_str[:-1]
        else:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)