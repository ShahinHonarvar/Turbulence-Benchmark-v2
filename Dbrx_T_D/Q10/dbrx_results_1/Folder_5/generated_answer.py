def all_odd_ints_exclusive(int_list):
    start, end = (2, 7)
    odds = [i for i in int_list[start:end] if i % 2 != 0]
    if start < len(int_list) < end:
        return odds[1:]
    else:
        return odds