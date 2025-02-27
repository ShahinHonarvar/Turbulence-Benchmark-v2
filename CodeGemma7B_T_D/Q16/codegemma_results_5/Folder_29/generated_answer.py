def sum_even_ints_inclusive(nums):
    even_nums = [num for num in nums[59:98] if num % 2 == 0]
    if not even_nums:
        return 0
    return sum(even_nums)