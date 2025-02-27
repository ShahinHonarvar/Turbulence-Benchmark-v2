def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[74]
    truncatable_primes = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        is_truncatable = True
        for i in range(len(num_str)):
            trunc_left = num_str[i:]
            trunc_right = num_str[:-i - 1] if i < len(num_str) - 1 else ''
            if trunc_left and (not is_prime(int(trunc_left))):
                is_truncatable = False
                break
            if trunc_right and (not is_prime(int(trunc_right))):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes