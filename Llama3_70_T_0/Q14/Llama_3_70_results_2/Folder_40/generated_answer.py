def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    smallest = min(numbers[:3])
    second_smallest = min((i for i in numbers[:3] if i != smallest))
    return second_smallest