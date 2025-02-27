def find_second_smallest_num(numbers):
    if 70 <= len(numbers) <= 200:
        sorted_numbers = sorted(numbers[70:201])
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    else:
        return None