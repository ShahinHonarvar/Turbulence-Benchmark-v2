def sum_even_ints_inclusive(nums):
    total = 0
    for num in nums[36:47]:
        if num % 2 == 0:
            total += num
    return total