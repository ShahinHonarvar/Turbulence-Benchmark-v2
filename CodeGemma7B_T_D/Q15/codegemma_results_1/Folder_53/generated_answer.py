def sum_odd_ints_inclusive(nums):
    if max(nums) - min(nums) < 300 or max(nums) < 300 or min(nums) > 300:
        raise ValueError('The sum range must fall between the indices 300 and 300 of the input list.')
    return sum((num for num in nums if num % 2 != 0 and num >= 300 and (num <= 300)))