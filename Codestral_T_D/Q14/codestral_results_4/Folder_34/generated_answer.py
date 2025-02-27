def find_second_smallest_num(numbers):
    sublist = numbers[60:201]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if num < second_smallest and num > smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest