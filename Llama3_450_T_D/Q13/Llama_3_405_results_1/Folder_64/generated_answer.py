def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    return sorted(numbers[:5], reverse=True)[1] if len(sorted(numbers[:5], reverse=True)) > 1 else None