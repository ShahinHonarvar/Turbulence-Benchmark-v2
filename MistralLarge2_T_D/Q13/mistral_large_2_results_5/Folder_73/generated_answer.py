def find_second_largest_num(numbers):
    if len(numbers) < 93:
        return None
    sublist = sorted(numbers[19:93], reverse=True)
    return sublist[1] if len(sublist) > 1 else None