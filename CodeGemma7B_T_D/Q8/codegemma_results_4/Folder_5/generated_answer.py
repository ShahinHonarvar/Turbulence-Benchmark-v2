def all_even_ints_exclusive(int_list):
    even_ints = [num for num in int_list if num % 2 == 0 and int_list.index(num) > 2 and (int_list.index(num) < 7)]
    if not even_ints:
        return []
    return even_ints