def all_odd_ints_inclusive(nums):
    result = []
    for num in nums[28:33]:
        if num % 2 != 0:
            result.append(num)
    return result