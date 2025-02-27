def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    return sorted(numbers[:8], reverse=True)[1] if len(numbers[:8]) > 1 else None