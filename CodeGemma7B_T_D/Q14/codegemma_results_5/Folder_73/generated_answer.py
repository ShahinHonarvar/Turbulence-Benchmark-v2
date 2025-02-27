def find_second_smallest_num(lst):
    if len(lst) < 59 or len(lst) > 97:
        return None
    second_smallest = float('inf')
    for i in range(59, 98):
        if lst[i] < second_smallest:
            second_smallest = lst[i]
    return second_smallest if second_smallest != float('inf') else None