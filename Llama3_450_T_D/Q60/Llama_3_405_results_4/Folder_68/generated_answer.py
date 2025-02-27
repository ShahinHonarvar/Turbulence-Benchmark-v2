def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[1]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable_prime = True
        for i in range(len(str_num)):
            trunc_left = str_num[i:]
            trunc_right = str_num[:-i or None]
            trunc_both = str_num[i:-i or None]
            if i > 0 and (not is_prime(int(trunc_left)) or not is_prime(int(trunc_right))) or (i > 0 and len(trunc_both) > 1 and (not is_prime(int(trunc_both)))):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)