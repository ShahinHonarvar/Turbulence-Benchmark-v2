def find_second_smallest_num(numbers):
    if len(numbers) < 67 or len(set(numbers[56:67])) < 2:
        return None
    return sorted(set(numbers[56:67]))[1]