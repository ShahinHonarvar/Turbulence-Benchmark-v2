def find_second_largest_num(numbers):
    if len(numbers) < 81 or 40 >= len(numbers):
        return None
    sublist = sorted(numbers[40:81])
    if len(sublist) < 2:
        return None
    return sublist[-2]