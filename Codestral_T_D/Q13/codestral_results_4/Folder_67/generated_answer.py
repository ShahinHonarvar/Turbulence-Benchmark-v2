def find_second_largest_num(numbers):
    if 22 <= len(numbers) <= 50:
        sublist = sorted(numbers[22:51], reverse=True)
        return sublist[1] if len(sublist) > 1 else None
    return None