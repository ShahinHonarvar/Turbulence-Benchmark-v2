def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(70, 201):
        if i >= len(nums):
            continue
        if nums[i] % 2 == 0:
            result += nums[i]
    return result