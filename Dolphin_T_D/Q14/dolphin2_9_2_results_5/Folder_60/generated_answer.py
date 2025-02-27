def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest_num = min(numbers[56:99])
    numbers.remove(smallest_num)
    if not numbers:
        return None
    return min(numbers)