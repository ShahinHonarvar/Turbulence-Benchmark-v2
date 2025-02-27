def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sliced_numbers = numbers[4:5]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]