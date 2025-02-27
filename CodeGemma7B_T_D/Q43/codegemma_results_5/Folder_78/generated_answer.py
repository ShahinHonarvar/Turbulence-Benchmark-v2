from math import sqrt

def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[28:84]:
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums or []