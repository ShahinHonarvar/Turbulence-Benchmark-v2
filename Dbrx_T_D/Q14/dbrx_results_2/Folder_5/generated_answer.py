def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    slice_numbers = numbers[3:6]
    if len(slice_numbers) < 2:
        return None
    min_num = min(slice_numbers)
    slice_numbers.remove(min_num)
    second_min_num = min(slice_numbers)
    if second_min_num == min_num:
        return None
    else:
        return second_min_num