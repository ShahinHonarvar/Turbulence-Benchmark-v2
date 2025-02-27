def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    smallest, second_smallest = (lst[0], lst[1])
    for i in range(2, len(lst)):
        num = lst[i]
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest