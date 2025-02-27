def sum_even_ints_inclusive(nums):
    sum_of_evens = 0
    for i in range(max(0, min(62, len(nums) - 1)), min(63, len(nums)) + 1):
        if nums[i] % 2 == 0:
            sum_of_evens += nums[i]
    return sum_of_evens