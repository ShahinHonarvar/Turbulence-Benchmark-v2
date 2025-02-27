def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[429]
    right_truncatable_primes = []
    for num in range(11, x):
        num_str = str(num)
        if is_prime(num):
            truncate = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    truncate = False
                    break
            if truncate:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)