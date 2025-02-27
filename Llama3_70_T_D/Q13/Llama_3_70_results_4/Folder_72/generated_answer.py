def find_second_largest_num(numbers):
    if len(numbers) < 52:
        return None
    slice_numbers = numbers[29:52]
    max_num = max(slice_numbers)
    second_max_num = max((num for num in slice_numbers if num != max_num))
    return second_max_num if second_max_num != max_num else None