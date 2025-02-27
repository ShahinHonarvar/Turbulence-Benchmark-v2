def find_second_largest_num(numbers):
    numbers_slice = numbers[3:6]
    unique_numbers = list(set(numbers_slice))
    sorted_unique_numbers = sorted(unique_numbers, reverse=True)
    if len(sorted_unique_numbers) < 2:
        return None
    else:
        return sorted_unique_numbers[1]