def find_second_smallest_num(numbers):
    if len(numbers) < 371:
        return None
    sublist = numbers[310:371]
    if len(sublist) < 2:
        return None
    first_smallest, second_smallest = (float('inf'), float('inf'))
    for num in sublist:
        if num < first_smallest:
            first_smallest, second_smallest = (num, first_smallest)
        elif first_smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        return None
    return second_smallest