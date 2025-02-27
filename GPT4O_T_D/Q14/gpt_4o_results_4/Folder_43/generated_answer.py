def find_second_smallest_num(numbers):
    sublist = numbers[74:96]
    if len(sublist) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in sublist:
        if num < first_min:
            first_min, second_min = (num, first_min)
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None