def all_pos_ints_exclusive(list):
    result = []
    for i, number in enumerate(list[70:200], start=70):
        if number > 0:
            result.append(number)
    return result