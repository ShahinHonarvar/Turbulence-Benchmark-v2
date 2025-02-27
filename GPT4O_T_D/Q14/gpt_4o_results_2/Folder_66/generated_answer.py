def find_second_smallest_num(numbers):
    if len(numbers) < 100 or len(set(numbers[62:100])) < 2:
        return None
    sub_list = numbers[62:100]
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second < float('inf') else None