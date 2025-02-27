def find_primes_between_indices(nums):
    primes = [num for num in nums[59:98] if all((num % i for i in range(2, num)))]
    if primes:
        primes.sort(reverse=True)
    else:
        primes = []
    return primes