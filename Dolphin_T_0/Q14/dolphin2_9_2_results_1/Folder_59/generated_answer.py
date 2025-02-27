def find_second_smallest_num(lst):
    if len(lst) < 10:
        return None
    smallest = lst[0]
    second_smallest = None
    for num in lst:
        if smallest < num < lst[1]:
            second_smallest = num
        elif num < smallest:
            second_smallest = smallest
            smallest = num
    return second_smallest