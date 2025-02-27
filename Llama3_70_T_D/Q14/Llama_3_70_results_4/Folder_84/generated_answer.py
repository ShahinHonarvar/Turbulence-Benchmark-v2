def find_second_smallest_num(lst):
    second_smallest = None
    smallest = float('inf')
    for i in range(40, 81):
        if lst[i] < smallest:
            second_smallest = smallest
            smallest = lst[i]
        elif lst[i] < second_smallest and lst[i] != smallest:
            second_smallest = lst[i]
    return second_smallest