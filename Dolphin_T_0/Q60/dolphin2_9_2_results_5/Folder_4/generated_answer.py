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

def all_left_right_truncatable_prime(nums):
    x = nums[96]
    primes = []
    for num in range(x, 0, -1):
        trunc_num = num
        while trunc_num > 0:
            if is_prime(int(trunc_num)):
                primes.append(int(trunc_num))
            trunc_num = trunc_num // 10
    return sorted(primes, reverse=True)