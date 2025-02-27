def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_truncatable = True
        for i in range(len(str_num)):
            trunc_left = int(str_num[i:])
            trunc_right = int(str_num[:len(str_num) - i])
            if not is_prime(trunc_left) or not is_prime(trunc_right):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)