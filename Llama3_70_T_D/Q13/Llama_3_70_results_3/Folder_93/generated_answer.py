def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    return sorted(numbers[75:95])[-2]