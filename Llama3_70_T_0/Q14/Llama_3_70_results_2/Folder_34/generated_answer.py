def find_second_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    second_smallest = min(numbers[60:201])
    numbers[60:201].remove(second_smallest)
    if len(numbers[60:201]) == 0:
        return None
    return min(numbers[60:201])