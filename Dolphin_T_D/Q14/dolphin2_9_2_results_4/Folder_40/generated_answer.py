def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    first_smallest = min(lst[0], lst[1], lst[2])
    second_smallest = max(lst[0], lst[1], lst[2])
    for i in range(3):
        if lst[i] != first_smallest and lst[i] < second_smallest:
            second_smallest = lst[i]
    if second_smallest == first_smallest:
        return None
    else:
        return second_smallest