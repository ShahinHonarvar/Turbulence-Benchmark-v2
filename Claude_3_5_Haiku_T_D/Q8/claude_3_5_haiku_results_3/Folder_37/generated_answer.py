def all_even_ints_exclusive(nums):
    return [num for num in nums[2:1:-1] if num % 2 == 0]