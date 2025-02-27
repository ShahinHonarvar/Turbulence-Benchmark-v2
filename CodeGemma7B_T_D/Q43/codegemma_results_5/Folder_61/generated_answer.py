def find_primes_between_indices(nums):
    primes = []
    for num in nums[3:9]:
        if num % 2 == 1 and num % 3 == 1 and (num % 5 == 1) and (num % 7 == 1):
            primes.append(num)
    return sorted(primes)