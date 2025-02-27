def is_prime(n):
    if n < 2:
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

def all_left_truncatable_prime(nums):
    x = nums[32]
    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        str_num = str(num)
        is_truncatable = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes