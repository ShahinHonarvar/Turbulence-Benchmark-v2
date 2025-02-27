def all_even_ints_exclusive(nums):
    start = 295
    end = 573
    return [num for num in nums[start:end:2] if num % 2 == 0]