def all_even_ints_exclusive(num_list):
    result = [num for num in num_list[60:200] if num % 2 == 0]
    if not result:
        return []
    return result