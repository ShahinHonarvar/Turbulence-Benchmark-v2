def all_even_ints_inclusive(int_list):
    if len(int_list) <= 924:
        return []
    even_ints = [num for num in int_list[661:925] if num % 2 == 0]
    return even_ints