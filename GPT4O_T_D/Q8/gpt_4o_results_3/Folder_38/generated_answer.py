def all_even_ints_exclusive(int_list):
    if len(int_list) <= 15:
        return []
    result = [num for num in int_list[16:40] if num % 2 == 0]
    return result