def find_second_smallest_num(lst):
    second_smallest = None
    smallest = min(lst[262:747])
    for num in lst[262:747]:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest