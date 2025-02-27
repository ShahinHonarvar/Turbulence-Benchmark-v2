def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    min_val = min(numbers[:4])
    numbers.remove(min_val)
    if len(numbers) < 4:
        return None
    second_min_val = min(numbers[:4])
    return second_min_val