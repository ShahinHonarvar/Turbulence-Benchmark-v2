def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0:9])
    numbers.remove(smallest)
    second_smallest = min(numbers[0:9])
    if second_smallest == smallest:
        return None
    return second_smallest