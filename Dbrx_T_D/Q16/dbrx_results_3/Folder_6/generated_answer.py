def sum_even_ints_inclusive(nums):
    start, end = (10, 66)
    nums = [num for num in nums[start:end + 1] if num % 2 == 0]
    return sum(nums) if nums else 0