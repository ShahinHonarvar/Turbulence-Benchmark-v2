def sum_odd_ints_inclusive(some_list):
    for i in range(len(some_list)):
        if i > 0:
            return sum((x for x in some_list[0:i + 1] if x % 2 != 0))
    return 0