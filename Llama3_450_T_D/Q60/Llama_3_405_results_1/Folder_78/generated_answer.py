def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[23]
    truncatable_primes = set()
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(1, len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))