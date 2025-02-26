def all_pos_ints_exclusive(integers):
    if len(integers) < 2:
        return []
    start = integers[0] + 1
    end = integers[1]
    return [num for num in range(start, end) if num > 0]