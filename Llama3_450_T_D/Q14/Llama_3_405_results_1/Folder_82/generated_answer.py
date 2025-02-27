def find_second_smallest_num(numbers):
    numbers = numbers[20:201]
    if len(numbers) < 2:
        return None
    return sorted(numbers)[1]