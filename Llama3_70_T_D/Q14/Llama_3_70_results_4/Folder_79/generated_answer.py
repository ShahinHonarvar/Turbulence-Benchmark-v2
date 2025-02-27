def find_second_smallest_num(numbers):
    sliced_numbers = numbers[1:6]
    sorted_numbers = sorted(sliced_numbers)
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]