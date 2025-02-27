def find_second_largest_num(numbers):
    sliced_numbers = numbers[4:5]
    if len(sliced_numbers) < 2:
        return None
    max_num = max(sliced_numbers)
    second_max_num = max((num for num in sliced_numbers if num != max_num))
    return second_max_num