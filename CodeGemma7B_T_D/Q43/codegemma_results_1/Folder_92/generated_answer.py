def find_primes_between_indices(nums):
    primes = []
    for num in nums[7:9]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)