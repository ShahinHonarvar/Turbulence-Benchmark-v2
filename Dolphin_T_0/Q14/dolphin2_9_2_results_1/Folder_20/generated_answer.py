def find_second_smallest_num(numbers):
    if len(numbers) <= 2:
        return None
    numbers = numbers[75:95]
    smallest = min(numbers)
    second_smallest = min(filter(lambda x: x != smallest, numbers))
    return second_smallest if second_smallest is not None else second_smallest