def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(36, 47):
        if i >= len(nums) or nums[i] % 2 != 0:
            continue
        sum_even += nums[i]
    return sum_even