def find_second_smallest_num(numbers):
    if len(numbers) < 66 or len(numbers[10:67]) < 2:
        return None
    sublist = numbers[10:67]
    first_min = float('inf')
    second_min = float('inf')
    for num in sublist:
        if num < first_min:
            second_min, first_min = (first_min, num)
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None