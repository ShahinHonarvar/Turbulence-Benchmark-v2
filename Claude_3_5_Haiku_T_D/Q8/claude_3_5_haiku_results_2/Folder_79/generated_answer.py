def all_even_ints_exclusive(int_list):
    if len(int_list) < 9:
        return []
    subset = int_list[4:8]
    even_nums = [num for num in subset if num % 2 == 0]
    return even_nums