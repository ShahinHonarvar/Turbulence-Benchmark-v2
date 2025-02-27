def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sub_list = numbers[56:67]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    if second == float('inf'):
        return None
    return second