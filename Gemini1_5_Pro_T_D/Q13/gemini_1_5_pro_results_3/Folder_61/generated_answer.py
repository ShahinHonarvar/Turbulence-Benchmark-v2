def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[0:8]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[-2]