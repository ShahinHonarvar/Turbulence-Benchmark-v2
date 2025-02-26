def find_second_smallest_num(numbers):
    if len(numbers) < 95 or len(numbers[75:95]) < 2:
        return None
    sublist = numbers[75:95]
    unique_sublist = sorted(set(sublist))
    return unique_sublist[1] if len(unique_sublist) >= 2 else None