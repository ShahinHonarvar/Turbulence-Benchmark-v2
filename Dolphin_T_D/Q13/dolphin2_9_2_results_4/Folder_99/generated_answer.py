def find_second_largest_num(elements):
    sublist = elements[310:371]
    if len(set(sublist)) < 2:
        return None
    else:
        first_max = max(sublist)
        sublist.remove(first_max)
        return max(sublist)