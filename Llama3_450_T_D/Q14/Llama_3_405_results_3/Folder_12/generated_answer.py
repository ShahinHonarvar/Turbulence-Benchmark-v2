def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    sliced_numbers = numbers[31:73]
    if len(sliced_numbers) < 2:
        return None
    sorted_numbers = sorted(sliced_numbers)
    return sorted_numbers[1]