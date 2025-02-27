import math

def find_primes_between_indices(nums):
    primes = []
    for i in range(187, 272):
        num = nums[i]
        if num > 1 and all((num % j != 0 for j in range(2, int(math.sqrt(num)) + 1))):
            primes.append(num)
    return sorted(primes)