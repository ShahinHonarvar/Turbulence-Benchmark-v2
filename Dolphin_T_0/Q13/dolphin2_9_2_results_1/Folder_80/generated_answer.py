def find_second_largest_num(lst):
    if 64 <= len(lst) <= 66:
        segment = lst[64:67]
        if len(segment) == 3:
            return sorted(segment)[-2]
        elif len(segment) == 2:
            return segment[0] if segment[1] > segment[0] else segment[1]
        elif len(segment) == 1:
            return None
    else:
        return None