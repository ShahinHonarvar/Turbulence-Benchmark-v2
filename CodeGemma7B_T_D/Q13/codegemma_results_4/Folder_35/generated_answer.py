def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers[30:49])
    if len(sorted_numbers) >= 2:
        return sorted_numbers[-2]
    return 'None'