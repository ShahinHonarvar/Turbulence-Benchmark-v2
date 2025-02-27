def sum_odd_ints_inclusive(nums):
    result = 0
    for num in nums[0:5]:
        if num % 2 == 1:
            result += num
    return result or 0