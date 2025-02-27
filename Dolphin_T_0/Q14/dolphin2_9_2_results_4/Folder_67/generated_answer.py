def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in lst[50:55]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None