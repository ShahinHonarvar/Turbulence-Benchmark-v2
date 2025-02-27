def find_second_largest_num(numbers):
    slice_numbers = numbers[62:100]
    if len(slice_numbers) < 2:
        return None
    max_num = max(slice_numbers)
    slice_numbers.remove(max_num)
    second_max = max(slice_numbers)
    return second_max