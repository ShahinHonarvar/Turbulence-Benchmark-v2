def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if '0' in str(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    str_num = str(n)
    length = len(str_num)
    for i in range(length):
        trunc_num = int(str_num[i:])
        if not is_prime(trunc_num):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[630]
    truncatable_primes = []
    for num in range(x, 11, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes