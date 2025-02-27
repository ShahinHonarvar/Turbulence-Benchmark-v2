def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    first_smallest = min(numbers[0:6])
    numbers.remove(first_smallest)
    if len(numbers) == 0:
        return None
    second_smallest = min(numbers)
    return second_smallest