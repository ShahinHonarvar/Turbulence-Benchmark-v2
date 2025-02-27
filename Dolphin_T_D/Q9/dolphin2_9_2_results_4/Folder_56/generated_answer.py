def all_odd_ints_inclusive(lst):
    inclusive_odd_list = []
    for i in range(lst[0], lst[1] + 1):
        if i % 2 != 0:
            inclusive_odd_list.append(i)
    return inclusive_odd_list