def all_ints_div_by_both_two_nums(nums):
    if not isinstance(nums, list) or not all((isinstance(num, int) for num in nums)):
        raise ValueError('Input must be a list of integers.')
    nums = [num for num in nums if num % 2 == 0 and num % 1 == 0]
    return nums