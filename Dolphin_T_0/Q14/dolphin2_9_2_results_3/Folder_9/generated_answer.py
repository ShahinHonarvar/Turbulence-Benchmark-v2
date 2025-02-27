def find_second_smallest_num(numbers):
    second_smallest_num = None
    for num in numbers[200:70:-1]:
        if second_smallest_num is None:
            second_smallest_num = num
        elif num < second_smallest_num:
            second_smallest_num = num
        elif num != second_smallest_num and second_smallest_num is not None:
            return second_smallest_num
    return second_smallest_num