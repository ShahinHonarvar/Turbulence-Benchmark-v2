def find_second_largest_num(numbers):
    slice_of_numbers = numbers[40:81]
    if len(slice_of_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in slice_of_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num