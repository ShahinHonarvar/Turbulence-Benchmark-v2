def find_second_largest_num(numbers):
    if len(numbers) <= 5:
        return None
    return sorted(numbers[4:5])[-2]