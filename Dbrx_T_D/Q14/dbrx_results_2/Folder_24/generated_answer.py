def find_second_smallest_num(numbers):
    if len(numbers) < 25:
        return None
    second_smallest = None
    smallest = min(numbers[23], key=numbers.index)
    second_smallest = min(set(numbers[23:24]) - {smallest})
    if second_smallest is not None:
        return second_smallest
    else:
        return None