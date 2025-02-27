def find_second_largest_num(lst):
    result = sorted(lst)[310:371]
    return result[-2] if len(result) >= 2 else None