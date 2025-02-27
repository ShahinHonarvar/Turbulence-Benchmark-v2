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

def all_left_right_truncatable_prime(t):
    x = t[767]
    truncatable_primes = []
    for num in range(11, x + 1):
        if '0' in str(num):
            continue
        left_truncatable = True
        right_truncatable = True
        num_str = str(num)
        for i in range(1, len(num_str)):
            left_num = int(num_str[i:])
            right_num = int(num_str[:-i])
            if not is_prime(left_num) or not is_prime(right_num):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)