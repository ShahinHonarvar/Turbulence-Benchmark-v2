def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    sub_list = numbers[:7]
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None