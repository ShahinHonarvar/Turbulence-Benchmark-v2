def find_primes_between_indices(nums):
    primes = []
    for num in nums[69:85]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes, reverse=True)