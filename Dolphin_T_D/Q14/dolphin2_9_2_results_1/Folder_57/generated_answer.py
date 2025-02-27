def find_second_smallest_num(lst):
    segment = lst[20:31]
    segment.sort()
    if len(segment) < 2:
        return None
    else:
        return segment[1]