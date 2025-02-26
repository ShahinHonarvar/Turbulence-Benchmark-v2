def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[55]
    right_truncatable_primes = []
    for num in range(x - 1, 1, -1):
        str_num = str(num)
        is_truncatable = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[:len(str_num) - i])
            if not is_prime(trunc_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)