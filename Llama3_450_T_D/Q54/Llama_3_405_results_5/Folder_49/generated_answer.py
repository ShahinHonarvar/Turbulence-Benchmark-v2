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

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    right_truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        is_right_truncatable = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[:-i or None])
            if not is_prime(trunc_num):
                is_right_truncatable = False
                break
        if is_right_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)