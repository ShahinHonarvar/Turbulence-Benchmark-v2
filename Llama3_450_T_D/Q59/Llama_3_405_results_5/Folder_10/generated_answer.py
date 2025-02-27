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

def all_left_truncatable_prime(numbers):
    x = numbers[38]
    left_truncatable_primes = []
    for num in range(10, x):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable = True
        for i in range(len(num_str)):
            trunc_num = int(num_str[i:])
            if not is_prime(trunc_num):
                truncatable = False
                break
        if truncatable and is_prime(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)