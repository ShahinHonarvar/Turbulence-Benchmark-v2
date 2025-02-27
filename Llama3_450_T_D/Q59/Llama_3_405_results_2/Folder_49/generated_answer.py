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

def all_left_truncatable_prime(nums):
    x = nums[14]
    truncatable_primes = []
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if is_prime(num):
            is_truncatable = True
            for i in range(1, len(str_num)):
                trunc_num = int(str_num[i:])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)