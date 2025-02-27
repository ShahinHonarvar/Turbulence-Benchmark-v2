def find_smallest_num(numbers):
    if len(numbers) < 3:
        return min(numbers)
    return min(numbers[0:3])