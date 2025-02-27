def find_smallest_num(numbers):
    if len(numbers) < 80:
        return None
    return min(numbers[29:80])