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

def all_right_truncatable_prime(nums):
    x = nums[11]
    right_truncatable_primes = []
    for num in range(11, x):
        str_num = str(num)
        is_right_truncatable_prime = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[:len(str_num) - i])
            if not is_prime(trunc_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)