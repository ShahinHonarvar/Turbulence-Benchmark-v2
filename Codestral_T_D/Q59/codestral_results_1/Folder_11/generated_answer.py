def all_left_truncatable_prime(numbers):
    x = numbers[86]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable = True
        truncated_num = num
        while truncated_num:
            if truncated_num not in left_truncatable_primes:
                is_truncatable = False
                break
            truncated_num //= 10
        if is_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)