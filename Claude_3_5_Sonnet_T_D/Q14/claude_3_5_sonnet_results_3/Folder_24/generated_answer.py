def find_second_smallest_num(numbers):
    if len(numbers) < 24 or len(numbers[23:24]) < 2:
        return None
    sorted_sublist = sorted(numbers[23:24])
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None