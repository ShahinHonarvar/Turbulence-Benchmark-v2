def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        return sorted(numbers[:5], reverse=True)[1] if len(set(numbers[:5])) > 1 else None