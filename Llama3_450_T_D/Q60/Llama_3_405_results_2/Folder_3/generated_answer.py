def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            truncatable = True
            for i in range(1, len(str_num)):
                trunc_left = int(str_num[i:])
                trunc_right = int(str_num[:-i])
                if not is_prime(trunc_left) or not is_prime(trunc_right):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)