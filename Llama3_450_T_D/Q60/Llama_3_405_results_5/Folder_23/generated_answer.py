def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:len(str_num) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                left_truncatable = False
                right_truncatable = False
                break
        if left_truncatable and right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)