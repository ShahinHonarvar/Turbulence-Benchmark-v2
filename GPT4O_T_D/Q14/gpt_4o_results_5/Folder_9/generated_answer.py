def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers[70:201]) < 2:
        return None
    sub_list = numbers[70:201]
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None