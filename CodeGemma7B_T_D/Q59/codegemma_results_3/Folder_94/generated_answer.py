def all_left_truncatable_prime(tup):
    x = tup[43]
    low = 0
    high = x - 1
    left_truncatable_primes = []
    while low <= high:
        mid = low + (high - low) // 2
        if is_prime(mid):
            if is_left_truncatable_prime(mid):
                left_truncatable_primes.append(mid)
        if mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return sorted(left_truncatable_primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        truncated_num = int(str_num[i:])
        if not is_prime(truncated_num):
            return False
    return True