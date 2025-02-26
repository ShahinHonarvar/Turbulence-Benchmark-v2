def all_pos_ints_exclusive(integers):
    if len(integers) < 3:
        return []
    start = integers[1] + 1
    end = integers[2]
    return [num for num in range(start, end) if num > 0]