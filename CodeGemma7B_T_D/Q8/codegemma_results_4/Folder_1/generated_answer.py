def all_even_ints_exclusive(nums):
    filtered_nums = [num for num in nums if num % 2 == 0 and 66 < num < 90]
    return filtered_nums if filtered_nums else []