def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest = min(lst[0], lst[1])
    second_smallest = max(lst[0], lst[1])
    for i in range(2, len(lst)):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
    if second_smallest == lst[0]:
        return second_smallest
    else:
        return None