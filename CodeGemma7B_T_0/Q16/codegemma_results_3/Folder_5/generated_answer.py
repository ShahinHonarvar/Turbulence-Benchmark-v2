def sum_even_ints_inclusive(nums):
    if not nums or len(nums) < 9 or (not nums[8] % 2) or (not nums[9] % 2):
        return 0
    return sum((num for num in nums[8:10] if num % 2 == 0))