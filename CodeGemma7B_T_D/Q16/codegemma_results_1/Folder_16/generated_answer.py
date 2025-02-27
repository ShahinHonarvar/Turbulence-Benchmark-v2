def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums[33:37]:
        if num % 2 == 0:
            total += num
    return total