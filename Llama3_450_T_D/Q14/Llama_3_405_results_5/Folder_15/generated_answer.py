def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:4]) < 2:
        return None
    return sorted(numbers[:4])[1]