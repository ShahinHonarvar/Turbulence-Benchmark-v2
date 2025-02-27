def find_primes_between_indices(nums):
    primes = []
    for num in nums[75:86:1]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes)