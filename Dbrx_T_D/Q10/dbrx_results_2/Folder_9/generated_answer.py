def all_odd_ints_exclusive(input_list):
    if len(input_list) < 72:
        return []
    result = []
    for i in input_list[70:72]:
        if i % 2 != 0:
            result.append(i)
    return result