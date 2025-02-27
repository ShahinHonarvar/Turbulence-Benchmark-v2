def find_second_smallest_num(numbers):
    sub_array = numbers[40:81]
    if len(sub_array) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_array:
        if num < first:
            second, first = (first, num)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None