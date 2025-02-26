def find_smallest_num(numbers):
    if len(numbers) < 10:
        return min(numbers)
    else:
        return min(numbers[:10])