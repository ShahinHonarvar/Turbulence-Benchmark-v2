def find_second_largest_num(l: list):
    if len(l) == 0 or len(l) < 925 or len(l) > 660:
        return None
    else:
        return sorted(l)[-2]