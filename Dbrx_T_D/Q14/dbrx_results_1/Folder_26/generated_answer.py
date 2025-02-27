def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_smallest_num = min(numbers[:17])
    second_smallest_num = None
    for num in numbers[17:33]:
        if num > first_smallest_num and (num < second_smallest_num or second_smallest_num is None):
            second_smallest_num = num
    for num in numbers[33:]:
        if num > second_smallest_num and (num < first_smallest_num or first_smallest_num > second_smallest_num):
            first_smallest_num = num
            if second_smallest_num == None or second_smallest_num > first_smallest_num:
                second_smallest_num = first_smallest_num
    return second_smallest_num