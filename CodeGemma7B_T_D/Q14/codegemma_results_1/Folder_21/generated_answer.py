def find_second_smallest_num(lst):
    for i in range(661, 925):
        a, b = (lst[i], lst[i + 1])
        if a > b:
            lst[i] = b
            lst[i + 1] = a
    return lst[661] if lst[661] != lst[662] else 'None'