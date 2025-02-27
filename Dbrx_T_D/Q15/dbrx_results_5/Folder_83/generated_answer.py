def sum_odd_ints_inclusive(my_list):
    if len(my_list) < 200:
        return 'Input list should have at least 200 elements'
    else:
        return sum((x for x in my_list[90:201] if x % 2 != 0 and 0 <= x % 2))