def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    return sorted(numbers[:3])[1]