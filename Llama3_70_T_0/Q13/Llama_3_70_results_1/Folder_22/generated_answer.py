def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        return sorted(numbers[40:201])[-2]