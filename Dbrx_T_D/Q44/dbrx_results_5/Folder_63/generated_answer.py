def composite_nums_between_indices(nums):
    if not isinstance(nums, list) or len(nums) < 78:
        return set()
    composite_nums = {num for num in nums[:78] if num > 1 and num % 2 == 0}
    primes = {2}
    for num in nums[:14]:
        if num not in primes:
            for prime in primes:
                if num % prime == 0:
                    break
            else:
                primes.add(num)
    composite_nums -= primes
    return composite_nums & set(nums[17:79])