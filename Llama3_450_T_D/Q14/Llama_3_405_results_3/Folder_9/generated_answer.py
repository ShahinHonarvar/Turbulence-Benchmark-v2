def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 71:
        return None
    return sorted(numbers[70:201])[1]