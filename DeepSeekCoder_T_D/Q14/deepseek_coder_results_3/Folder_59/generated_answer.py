def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 10:
        return None
    sorted_slice = sorted(numbers[:10])
    return sorted_slice[1] if len(sorted_slice) > 1 else None