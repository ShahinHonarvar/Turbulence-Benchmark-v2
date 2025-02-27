def sum_odd_ints_inclusive(nums):
    result = 0
    for num in nums:
        if num % 2 != 0 and num in range(len(nums)):
            result += num
    if result == 0:
        return 0
    return result