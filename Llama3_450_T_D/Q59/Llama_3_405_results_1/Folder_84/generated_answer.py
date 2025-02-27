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

def all_left_truncatable_prime(numbers):
    x = numbers[630]
    left_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_truncatable = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[i:])
            if not is_prime(trunc_num):
                is_left_truncatable = False
                break
        if is_left_truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)