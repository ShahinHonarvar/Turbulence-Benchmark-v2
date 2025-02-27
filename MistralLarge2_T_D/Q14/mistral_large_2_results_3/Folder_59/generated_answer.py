def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in numbers[:10]:
        if num < first_min:
            first_min, second_min = (num, first_min)
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None