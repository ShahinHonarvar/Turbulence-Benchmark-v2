def find_second_smallest_num(lst):
    sublist = lst[10:67]
    if len(sublist) < 2:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num > smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None