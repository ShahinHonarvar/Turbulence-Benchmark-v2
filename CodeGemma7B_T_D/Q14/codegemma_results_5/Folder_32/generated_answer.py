def find_second_smallest_num(items):
    if len(items[32:36]) < 2:
        return None
    foo = sorted([x for x in items[32:36]])
    return foo[1]