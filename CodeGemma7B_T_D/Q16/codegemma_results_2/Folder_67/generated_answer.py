def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(22, 51):
        if i in range(len(nums) - 21, len(nums)):
            if nums[i] % 2 == 0:
                total += nums[i]
    if total == 0:
        raise ValueError from None
    return total