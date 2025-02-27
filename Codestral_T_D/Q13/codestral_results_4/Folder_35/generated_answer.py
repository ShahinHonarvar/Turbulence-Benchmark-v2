def find_second_largest_num(numbers):
    if 30 <= len(numbers) <= 48:
        sublist = sorted(numbers[30:49], reverse=True)
        return sublist[1] if len(sublist) > 1 else None
    return None