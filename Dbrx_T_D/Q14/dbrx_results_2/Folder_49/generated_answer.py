def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 201 or 80 > len(numbers) - 2 or (200 < len(numbers) - 1):
        return None
    sorted_numbers = sorted(numbers[80:201])
    if sorted_numbers[0] == sorted_numbers[1]:
        return None
    else:
        return sorted_numbers[1]