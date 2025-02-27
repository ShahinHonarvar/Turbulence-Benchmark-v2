def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[43]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            truncatable = True
            for i in range(len(num_str)):
                trunc_str = num_str[:-i - 1]
                if trunc_str and (not is_prime(int(trunc_str))):
                    truncatable = False
                    break
            if truncatable and len(num_str) > 1:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)