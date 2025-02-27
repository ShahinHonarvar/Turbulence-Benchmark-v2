def sum_even_ints_inclusive(nums):
    result = 0
    for num in nums[75:86]:
        if num % 2 == 0:
            result += num
    return result or 0