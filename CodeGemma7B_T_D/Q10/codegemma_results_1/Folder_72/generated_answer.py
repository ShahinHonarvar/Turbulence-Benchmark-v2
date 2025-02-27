def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[56:88]:
        if num % 2 != 0:
            result.append(num)
    return result