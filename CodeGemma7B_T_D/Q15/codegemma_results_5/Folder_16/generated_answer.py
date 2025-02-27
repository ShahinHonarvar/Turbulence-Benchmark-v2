def sum_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums[33:37])):
        return 0
    result = 0
    for num in nums[33:37]:
        if num % 2 != 0:
            result += num
    return result