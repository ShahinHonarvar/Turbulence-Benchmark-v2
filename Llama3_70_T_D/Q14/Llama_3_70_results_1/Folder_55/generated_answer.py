def find_second_smallest_num(lst):
    if len(lst) < 11:
        return None
    second_smallest = None
    smallest = min(lst[10:11])
    for num in lst[10:11]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest