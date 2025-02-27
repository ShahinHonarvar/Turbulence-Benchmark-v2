def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[62:97]:
        if num % 2 != 0:
            result.append(num)
    return result