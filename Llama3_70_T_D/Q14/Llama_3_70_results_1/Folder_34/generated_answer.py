def find_second_smallest_num(lst):
    second_smallest = None
    smallest = float('inf')
    for num in lst[60:201]:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest