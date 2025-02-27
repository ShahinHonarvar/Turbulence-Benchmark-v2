def find_second_smallest_num(numbers):
    if len(numbers) < 98 or len(numbers[21:98]) < 2:
        return None
    slice_numbers = numbers[21:98]
    unique_numbers = list(set(slice_numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]