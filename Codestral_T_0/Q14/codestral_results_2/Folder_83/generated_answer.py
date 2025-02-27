def find_second_smallest_num(numbers):
    if 90 <= len(numbers) <= 200:
        sorted_numbers = sorted(numbers[90:201])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None