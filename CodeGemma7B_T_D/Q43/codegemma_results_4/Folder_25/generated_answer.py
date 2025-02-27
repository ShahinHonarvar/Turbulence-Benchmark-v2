def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[52:54]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums or []