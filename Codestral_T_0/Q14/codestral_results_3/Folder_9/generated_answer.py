def find_second_smallest_num(numbers):
    if 70 <= len(numbers) <= 200:
        sorted_numbers = sorted(numbers[70:201])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None