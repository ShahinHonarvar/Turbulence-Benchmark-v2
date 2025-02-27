def all_even_ints_exclusive(nums):
    slice_nums = nums[49:74]
    even_nums = [num for num in slice_nums if num % 2 == 0]
    return even_nums