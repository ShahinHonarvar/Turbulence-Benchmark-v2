def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    else:
        return sorted(numbers[5:8])[1]