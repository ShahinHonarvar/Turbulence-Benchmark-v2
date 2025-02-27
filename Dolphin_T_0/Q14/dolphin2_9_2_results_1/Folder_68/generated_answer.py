def find_second_smallest_num(lst):
    if len(lst) <= 1:
        return None
    smallest = second_smallest = float('inf')
    for i in range(len(lst) <= 8):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
    return second_smallest if second_smallest != float('inf') else None