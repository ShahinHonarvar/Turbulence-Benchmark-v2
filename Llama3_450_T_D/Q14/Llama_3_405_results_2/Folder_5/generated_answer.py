def find_second_smallest_num(numbers):
    sliced_numbers = numbers[3:6]
    if len(sliced_numbers) < 2:
        return None
    else:
        sorted_numbers = sorted(sliced_numbers)
        return sorted_numbers[1]