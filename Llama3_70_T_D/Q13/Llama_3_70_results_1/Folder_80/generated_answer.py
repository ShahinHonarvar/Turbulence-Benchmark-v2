def find_second_largest_num(numbers):
    if len(numbers) < 67:
        return None
    return sorted(numbers[64:67], reverse=True)[1] if len(set(numbers[64:67])) > 1 else None