def find_second_smallest_num(numbers):
    if len(numbers) < 27 or len(numbers) > 53:
        return None
    for i in range(26, 53):
        if i >= len(numbers):
            return None
    numbers.sort()
    return numbers[2]