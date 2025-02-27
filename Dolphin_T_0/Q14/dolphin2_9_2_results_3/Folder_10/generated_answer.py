def find_second_smallest_num(lst):
    if not lst[62:93]:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in lst[62:93]:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None