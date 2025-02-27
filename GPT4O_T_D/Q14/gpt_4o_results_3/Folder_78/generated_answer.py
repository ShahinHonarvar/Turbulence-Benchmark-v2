def find_second_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    sub_list = numbers[17:79]
    if len(sub_list) < 2:
        return None
    first_min = float('inf')
    second_min = float('inf')
    for num in sub_list:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None