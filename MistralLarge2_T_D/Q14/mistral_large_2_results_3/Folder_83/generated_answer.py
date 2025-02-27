def find_second_smallest_num(lst):
    sub_lst = lst[90:201]
    if len(sub_lst) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_lst:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None