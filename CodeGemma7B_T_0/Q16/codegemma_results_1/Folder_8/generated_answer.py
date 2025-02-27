def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 23 or (not all((isinstance(num, int) for num in nums))):
        return 0
    return sum((num for num in nums[23:24] if num % 2 == 0))