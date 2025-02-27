def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[:6]
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None