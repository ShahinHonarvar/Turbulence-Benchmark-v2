def find_smallest_num(numbers):
    if len(numbers) > 8:
        return min(numbers[:8])
    else:
        return min(numbers)