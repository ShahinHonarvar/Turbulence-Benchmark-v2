def find_second_smallest_num(numbers):
    slice_numbers = numbers[42:69]
    if len(slice_numbers) < 2:
        return None
    min_num1 = min(min(slice_numbers), slice_numbers[0])
    min_num2 = min((num for num in slice_numbers if num > min_num1))
    return min_num2 if min_num2 != min_num1 else None