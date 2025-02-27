def sum_odd_ints_inclusive(nums):
    valid_nums = nums[527:539]
    odd_nums = [num for num in valid_nums if num % 2 != 0]
    if not odd_nums:
        return 0
    return sum(odd_nums)