def find_second_smallest_num(lst):
    second_smallest = None
    for num in lst[55:99]:
        if second_smallest is None and num is not None:
            second_smallest = num
        elif num is not None and num < second_smallest:
            second_smallest = num
    return second_smallest