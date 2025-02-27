def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers)
    second_smallest = min((i for i in numbers if i != smallest))
    return second_smallest