def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 2:
        return None
    sorted_numbers = sorted(numbers[80:201], reverse=True)
    if len(sorted_numbers) < 2:
        return None
    return sorted_numbers[1]