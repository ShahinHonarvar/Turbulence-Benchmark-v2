def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 2 or max(numbers) <= 1 or (100 not in range(len(numbers))):
        return 'None'
    sorted_numbers = sorted(numbers[1:101])
    return sorted_numbers[1] if len(sorted_numbers) >= 2 else 'None'