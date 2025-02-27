def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    else:
        return sorted(numbers[15:40])[1]