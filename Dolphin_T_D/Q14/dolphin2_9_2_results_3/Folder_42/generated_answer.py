def find_second_smallest_num(lst):
    if len(lst) == 0 or len(lst) < 22 or len(lst) > 97:
        return None
    second_smallest = None
    smallest = float('inf')
    for num in lst[21:98]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest