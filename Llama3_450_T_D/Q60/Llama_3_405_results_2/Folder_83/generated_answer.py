def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        truncatable = True
        for i in range(len(str_num)):
            left_trunc = int(str_num[i:])
            right_trunc = int(str_num[:len(str_num) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                truncatable = False
                break
        if truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)