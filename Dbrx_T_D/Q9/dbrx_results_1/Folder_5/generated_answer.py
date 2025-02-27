def all_odd_ints_inclusive(int_list):
    if len(int_list) >= 10:
        start, end = (8, 9)
        return [num for num in int_list[start:end + 1] if num % 2 != 0]
    else:
        return []