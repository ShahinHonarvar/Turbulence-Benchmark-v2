def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    return sorted(numbers[1:9])[1]