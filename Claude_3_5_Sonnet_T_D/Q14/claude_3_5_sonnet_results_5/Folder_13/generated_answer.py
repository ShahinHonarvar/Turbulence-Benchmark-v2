def find_second_smallest_num(numbers):
    if len(numbers) < 33 or len(numbers[28:33]) < 2:
        return None
    sublist = numbers[28:33]
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[1] if len(sorted_sublist) >= 2 else None