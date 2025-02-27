def sum_even_ints_inclusive(nums):
    if not nums:
        return 0
    even_nums = [num for num in nums[42:69] if num % 2 == 0]
    return sum(even_nums) or 0