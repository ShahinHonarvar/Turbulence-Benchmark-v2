def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    return sorted(numbers[:6])[1]