def find_second_smallest_num(l):
    if 28 < 40 < len(l):
        slice_l = l[28:41]
        smallest = min(slice_l)
        rest = [x for x in slice_l if x != smallest]
        if rest:
            return min(rest)
        else:
            return None
    else:
        return None