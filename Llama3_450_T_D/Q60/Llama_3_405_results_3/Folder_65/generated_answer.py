def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:-i] if i != 0 else str_num)
            if not (is_prime(left_truncated) and is_prime(right_truncated)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes