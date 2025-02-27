def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[36:85]:
        if num % 2 != 0:
            result.append(num)
    return result or []