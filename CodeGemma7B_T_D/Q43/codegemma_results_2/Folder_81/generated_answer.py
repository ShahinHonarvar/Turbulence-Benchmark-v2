def find_primes_between_indices(nums):
    primes = []
    for num in nums[59:98]:
        if num % 2 != 0 and all((num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2))):
            primes.append(num)
    return sorted(primes, reverse=True)