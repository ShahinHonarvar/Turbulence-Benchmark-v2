def find_second_smallest_num(numbers):
    if len(numbers) < 93 or not numbers:
        return None
    sublist = numbers[62:93]
    if len(sublist) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in sublist:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None