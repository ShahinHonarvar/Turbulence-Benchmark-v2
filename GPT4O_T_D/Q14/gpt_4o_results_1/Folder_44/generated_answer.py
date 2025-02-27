def find_second_smallest_num(numbers):
    if len(numbers) < 100:
        return None
    segment = numbers[91:100]
    if len(segment) < 2:
        return None
    first_min = second_min = float('inf')
    for num in segment:
        if num < first_min:
            second_min, first_min = (first_min, num)
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None