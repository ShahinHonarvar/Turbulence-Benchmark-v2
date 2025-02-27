def find_second_smallest_num(lst):
    second_smallest = None
    try:
        segment = sorted(lst[608:610])
        if len(segment) > 1:
            second_smallest = segment[1]
    except IndexError:
        pass
    return second_smallest