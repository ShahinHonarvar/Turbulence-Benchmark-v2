def find_second_smallest_num(lst):
    slice = lst[36:47]
    if len(slice) < 2:
        return None
    smallest, second_smallest = (slice[0], None)
    for num in slice:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif num != smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest