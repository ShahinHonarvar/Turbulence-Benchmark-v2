def all_pos_ints_inclusive(lst):
    output = []
    for num in lst:
        if num > 0 and 4 <= lst.index(num) <= 4:
            output.append(num)
    if not output:
        return []
    return output