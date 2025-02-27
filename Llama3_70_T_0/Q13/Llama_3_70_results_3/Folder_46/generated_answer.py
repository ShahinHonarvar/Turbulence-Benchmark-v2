def find_second_largest_num(numbers):
    if len(numbers) < 88:
        return None
    else:
        return sorted(numbers[30:88])[-2]