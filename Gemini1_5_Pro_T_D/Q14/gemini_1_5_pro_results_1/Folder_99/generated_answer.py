def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    else:
        return sorted(numbers[608:610])[1]