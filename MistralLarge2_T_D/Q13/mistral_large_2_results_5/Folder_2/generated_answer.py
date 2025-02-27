def find_second_largest_num(numbers):
    if len(numbers) <= 39:
        return None
    sublist = sorted(numbers[15:40])
    if len(sublist) < 2:
        return None
    return sublist[-2]