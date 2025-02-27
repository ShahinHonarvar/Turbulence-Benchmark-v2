def find_smallest_num(lst):
    if len(lst) < 80:
        return None
    smallest = float('inf')
    for i in range(80, 81):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest