def find_second_largest_num(numbers):
    if len(numbers) < 72:
        return None
    sublist = numbers[52:72]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]