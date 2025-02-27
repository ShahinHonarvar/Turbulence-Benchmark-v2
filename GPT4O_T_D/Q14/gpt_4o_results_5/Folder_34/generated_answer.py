def find_second_smallest_num(numbers):
    if len(numbers) < 201 or 60 > len(numbers) - 1:
        return None
    subset = numbers[60:201]
    if len(subset) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in subset:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    if second_min == float('inf'):
        return None
    return second_min