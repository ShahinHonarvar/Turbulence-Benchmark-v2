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
    x = numbers[54]
    truncatable_primes = set()
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        is_truncatable = True
        for i in range(1, len(str_num)):
            trunc_num = int(str_num[i:])
            if not is_prime(trunc_num):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes))