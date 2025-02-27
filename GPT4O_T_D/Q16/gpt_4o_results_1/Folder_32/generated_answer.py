def sum_even_ints_inclusive(nums):
    if not isinstance(nums, list) or not all((isinstance(i, int) for i in nums)):
        return 0
    return sum((x for x in nums[21:98] if x % 2 == 0))