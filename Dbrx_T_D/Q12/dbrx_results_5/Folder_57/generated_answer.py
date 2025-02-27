def find_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    else:
        return min(numbers[27:40])