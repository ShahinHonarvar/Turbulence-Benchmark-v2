def all_odd_ints_inclusive(nums):
    result = []
    for num in nums[25:60]:
        if num % 2 != 0:
            result.append(num)
    return result