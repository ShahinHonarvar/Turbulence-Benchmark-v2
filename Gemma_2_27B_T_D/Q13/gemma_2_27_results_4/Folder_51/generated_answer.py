def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sorted_numbers = sorted(numbers[1:9], reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]