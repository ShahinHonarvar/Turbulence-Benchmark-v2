def find_second_smallest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 9:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in numbers[:9]:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None