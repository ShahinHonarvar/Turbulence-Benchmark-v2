def find_second_largest_num(numbers):
    sublist = sorted(numbers[27:56])[-2:]
    return sublist[-2] if len(sublist) == 2 else None