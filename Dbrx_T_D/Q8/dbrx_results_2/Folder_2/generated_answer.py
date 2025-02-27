def all_even_ints_exclusive(int_list):
    start = 36
    end = 52
    if start < 0 or end > len(int_list) or end < start:
        return []
    return [num for num in int_list[start:end] if num % 2 == 0]