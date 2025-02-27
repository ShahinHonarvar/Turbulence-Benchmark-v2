def find_second_smallest_num(lst):
    if len(lst) < 64:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in lst[22:64]:
        if smallest > num > second_smallest:
            second_smallest = num
        elif smallest == float('inf') and num != min(lst[22:64]):
            smallest = num
            second_smallest = min(lst[22:64])
    return second_smallest