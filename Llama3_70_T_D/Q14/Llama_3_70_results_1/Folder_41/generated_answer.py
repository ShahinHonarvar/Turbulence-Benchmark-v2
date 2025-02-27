def find_second_smallest_num(numbers):
    sliced_numbers = numbers[4:5]
    if len(sliced_numbers) == 0:
        return None
    else:
        return min(sliced_numbers)