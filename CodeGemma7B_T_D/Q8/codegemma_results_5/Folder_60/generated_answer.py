def all_even_ints_exclusive(list_of_nums):
    even_nums = [num for num in list_of_nums[44:91] if num % 2 == 0]
    return even_nums if even_nums else []