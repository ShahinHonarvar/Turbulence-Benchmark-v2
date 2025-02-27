def all_even_ints_inclusive(nums):
    even_nums = [num for num in nums[29:79 + 1] if num % 2 == 0]
    return even_nums if even_nums else []