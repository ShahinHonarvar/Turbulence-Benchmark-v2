def find_second_largest_num(depths):
    if len(depths) < 2:
        return None
    largest, second_largest = (depths[0], None)
    for depth in depths:
        if depth > largest:
            second_largest, largest = (largest, depth)
        elif depth != largest and (second_largest is None or depth > second_largest):
            second_largest = depth
    return second_largest if second_largest != None else None