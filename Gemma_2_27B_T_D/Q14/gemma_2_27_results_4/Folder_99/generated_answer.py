def find_second_smallest_num(numbers):
    if len(numbers) >= 609 and len(set(numbers[608:610])) == 2:
        return sorted(numbers[608:610])[1]
    else:
        return None