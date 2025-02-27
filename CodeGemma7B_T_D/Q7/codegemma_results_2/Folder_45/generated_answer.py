def all_even_ints_inclusive(lst):
    nums = lst[30:201]
    even_nums = [num for num in nums if num % 2 == 0]
    return even_nums if even_nums else []