def find_second_smallest_num(lst):
    if len(lst) >= 87 and len(lst[68:87]) >= 2:
        second_smallest = min(lst[68:87])
        for num in lst[68:87]:
            if num < second_smallest and num != min(lst[68:87]):
                second_smallest = num
        return second_smallest
    else:
        return None