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
    x = numbers[39]
    truncatable_primes = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            trunc_left = str_num[i:]
            trunc_right = str_num[:len(str_num) - i]
            if len(trunc_left) > 1 and (not is_prime(int(trunc_left))):
                is_truncatable = False
                break
            if len(trunc_right) > 1 and (not is_prime(int(trunc_right))):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)