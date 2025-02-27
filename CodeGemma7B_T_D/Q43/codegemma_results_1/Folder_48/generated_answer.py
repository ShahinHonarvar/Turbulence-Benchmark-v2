import math

def find_primes_between_indices(nums):
    primes = []
    for num in nums[261:460]:
        flag = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
        if flag and num != 1:
            primes.append(num)
    primes.sort()
    return primes or []