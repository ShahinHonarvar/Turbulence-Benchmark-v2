def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[10:67]:
        if num in [1, 0]:
            continue
        if all((num % x != 0 for x in range(2, num))):
            prime_nums.append(num)
    return prime_nums or []