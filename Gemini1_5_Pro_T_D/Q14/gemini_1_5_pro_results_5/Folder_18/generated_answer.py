def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    else:
        sliced_numbers = numbers[30:49]
        sorted_numbers = sorted(sliced_numbers)
        return sorted_numbers[1]