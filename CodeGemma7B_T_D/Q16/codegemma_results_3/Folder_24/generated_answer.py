def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(74, 96):
        if i >= len(nums):
            break
        num = nums[i]
        if num % 2 == 0:
            total += num
    return total