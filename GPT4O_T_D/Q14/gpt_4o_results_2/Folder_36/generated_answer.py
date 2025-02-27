def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    sub_list = numbers[209:557]
    if len(sub_list) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for n in sub_list:
        if n < first:
            first, second = (n, first)
        elif first < n < second:
            second = n
    return second if second < float('inf') else None