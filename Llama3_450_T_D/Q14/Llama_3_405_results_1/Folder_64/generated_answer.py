def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    smallest = min(numbers[:5])
    second_smallest = min((x for x in numbers[:5] if x != smallest), default=None)
    return second_smallest