from math import sqrt

def all_right_truncatable_prime(nums):
    x = nums[37]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:-i])):
                return False
        return True
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num) and is_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)