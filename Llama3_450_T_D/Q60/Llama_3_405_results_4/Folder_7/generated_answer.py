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

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            left_trunc = str_num[i:]
            right_trunc = str_num[:-i or None]
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)