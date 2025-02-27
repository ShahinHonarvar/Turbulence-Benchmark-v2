def find_second_smallest_num(numbers):
    if len(numbers) <= 200 or len(numbers[90:201]) < 2:
        return None
    sub_list = numbers[90:201]
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None