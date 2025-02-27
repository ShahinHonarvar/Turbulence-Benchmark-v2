def find_second_smallest_num(lst):
    second_smallest = lst[1:101]
    second_smallest.sort()
    if len(second_smallest) < 2:
        return None
    else:
        return second_smallest[1]