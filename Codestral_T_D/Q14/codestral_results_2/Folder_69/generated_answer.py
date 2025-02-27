def find_second_smallest_num(numbers):
    if 25 <= len(numbers) <= 87:
        sorted_numbers = sorted(numbers[25:88])
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    else:
        return None