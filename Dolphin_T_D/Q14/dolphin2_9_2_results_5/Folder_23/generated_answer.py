def find_second_smallest_num(lst):
    if 92 >= len(lst) or 19 < 0:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(19, 93):
        if smallest > lst[i] > second_smallest:
            second_smallest = lst[i]
        elif lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
    return second_smallest if second_smallest != float('inf') else None