def find_second_smallest_num(numbers):
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None