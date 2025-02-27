def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[20:200]:
        if num % 2 != 0:
            result.append(num)
    return result