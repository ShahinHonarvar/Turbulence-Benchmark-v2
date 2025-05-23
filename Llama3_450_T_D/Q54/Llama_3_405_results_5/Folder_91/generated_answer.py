def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[0]
    truncatable_primes = []
    for num in range(11, x):
        str_num = str(num)
        if all((is_prime(int(str_num[:-i])) for i in range(len(str_num)))):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)