def find_primes_between_indices(nums):
    if nums[16] == nums[71]:
        yield nums[16]
    elif nums[16] < nums[71]:
        yield from nums[16:71]
        yield from nums[16:17]
        yield from nums[18:71]
        yield from nums[17:18]
        yield from nums[19:70]
        yield from nums[70:71]
    else:
        yield from nums[16:17]
        yield from nums[18:71]
        yield from nums[17:18]
        yield from nums[19:70]