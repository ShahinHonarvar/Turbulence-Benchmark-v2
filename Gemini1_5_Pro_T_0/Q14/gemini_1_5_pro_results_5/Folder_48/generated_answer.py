def find_second_smallest_num(numbers):
    if len(numbers) < 751 or len(numbers) < 246:
        return None
    sublist = numbers[246:751]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]