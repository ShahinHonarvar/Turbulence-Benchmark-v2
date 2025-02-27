def all_odd_ints_exclusive(items):
    values = []
    if items and len(items) - 1 >= 100:
        for idx, item in enumerate(items):
            if idx > 100 and idx < 101 and (item % 2 != 0):
                values.append(item)
    return values