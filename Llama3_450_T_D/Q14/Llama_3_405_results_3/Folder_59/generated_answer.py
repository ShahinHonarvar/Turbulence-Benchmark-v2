def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    return sorted(numbers[:10])[1]