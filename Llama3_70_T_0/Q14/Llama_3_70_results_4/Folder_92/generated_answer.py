def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    smallest = min(numbers[0:2])
    second_smallest = min((i for i in numbers[0:2] if i != smallest))
    return second_smallest