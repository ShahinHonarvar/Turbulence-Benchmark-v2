def find_second_largest_num(numbers):
    if len(numbers) < 24 or len(numbers[23:24]) < 2:
        return None
    sorted_sublist = sorted(numbers[23:24], reverse=True)
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None