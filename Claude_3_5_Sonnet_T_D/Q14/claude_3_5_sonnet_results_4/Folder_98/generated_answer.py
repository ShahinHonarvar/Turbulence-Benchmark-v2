def find_second_smallest_num(numbers):
    if len(numbers) < 7 or len(numbers[6:7]) < 2:
        return None
    sorted_sublist = sorted(numbers[6:7])
    return sorted_sublist[1] if len(sorted_sublist) > 1 else None