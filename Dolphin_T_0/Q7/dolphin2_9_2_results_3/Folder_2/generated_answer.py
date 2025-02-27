def all_even_ints_inclusive(lst):
    even_nums = [num for num in lst[15:40] if num % 2 == 0]
    if not even_nums:
        return []
    else:
        return even_nums