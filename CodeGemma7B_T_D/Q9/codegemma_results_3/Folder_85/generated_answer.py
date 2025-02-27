def all_odd_ints_inclusive(num_list):
    output = []
    _begin = 6
    _end = 9
    for i in num_list[_begin:_end + 1]:
        if i % 2 != 0:
            output.append(i)
    if not output:
        return []
    return output