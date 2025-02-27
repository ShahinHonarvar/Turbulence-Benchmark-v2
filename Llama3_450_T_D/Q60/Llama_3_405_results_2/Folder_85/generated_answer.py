def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[94]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        str_num = str(num)
        for i in range(len(str_num)):
            trunc_left_right = str_num[i:-i] if i < len(str_num) - i else ''
            if len(trunc_left_right) > 1:
                if not is_prime(int(trunc_left_right)):
                    break
            elif len(trunc_left_right) == 1:
                if not is_prime(int(trunc_left_right)):
                    break
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)