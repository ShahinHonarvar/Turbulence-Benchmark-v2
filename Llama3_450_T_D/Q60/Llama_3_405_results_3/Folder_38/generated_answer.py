def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        left_right_truncatable = True
        for i in range(len(str_num)):
            trunc_left = int(str_num[i:])
            trunc_right = int(str_num[:-i or None])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes