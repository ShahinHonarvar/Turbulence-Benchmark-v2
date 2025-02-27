def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[276:376]:
        if num % 2 == 1:
            result.append(num)
    return result