def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(t):
    x = t[1]
    left_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)