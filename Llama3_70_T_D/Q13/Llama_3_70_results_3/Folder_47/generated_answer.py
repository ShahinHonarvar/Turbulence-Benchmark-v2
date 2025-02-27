def find_second_largest_num(numbers):
    slice_numbers = numbers[37:77]
    if len(slice_numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in slice_numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max