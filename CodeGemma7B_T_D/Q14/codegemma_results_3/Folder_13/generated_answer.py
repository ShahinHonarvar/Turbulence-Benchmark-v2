def find_second_smallest_num(l: list) -> int | None:
    if not l or len(l) <= 28:
        return None
    l = sorted(l[28:33])
    if len(l) < 2:
        return None
    return l[1]