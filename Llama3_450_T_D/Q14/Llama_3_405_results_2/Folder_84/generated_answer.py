def find_second_smallest_num(numbers):
    if len(numbers) < 81 or 40 > len(numbers) - 1:
        return None
    sliced_numbers = numbers[40:81]
    if len(sliced_numbers) < 2:
        return None
    return sorted(sliced_numbers)[1]