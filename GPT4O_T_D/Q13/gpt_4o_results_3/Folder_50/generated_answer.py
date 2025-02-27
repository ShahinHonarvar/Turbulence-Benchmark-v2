def find_second_largest_num(numbers):
    if len(numbers) < 85:
        return None
    sublist = numbers[70:85]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[-2]