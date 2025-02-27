def find_second_smallest_num(numbers):
    sublist = numbers[1:6]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = float('inf')
    for num in sublist:
        if num > smallest and num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest