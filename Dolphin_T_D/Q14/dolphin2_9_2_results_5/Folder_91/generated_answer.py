def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for i in lst[0:6]:
        if i < smallest:
            second_smallest, smallest = (smallest, i)
        elif i < second_smallest and i != smallest:
            second_smallest = i
    return second_smallest if second_smallest != float('inf') else None