def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[93]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            num_str = str(num)
            for i in range(1, len(num_str)):
                trunc_left = int(num_str[i:])
                trunc_right = int(num_str[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    break
            else:
                truncatable_primes.append(num)
    return truncatable_primes