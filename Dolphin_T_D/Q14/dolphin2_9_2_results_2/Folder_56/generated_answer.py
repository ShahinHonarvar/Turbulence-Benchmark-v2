def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    else:
        smallest = lst[0]
        second_smallest = None
        for num in lst:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num != smallest and (second_smallest is None or num < second_smallest):
                second_smallest = num
        return second_smallest