def find_second_largest_num(numbers):
    if len(numbers) < 98:
        return None
    sublist = sorted(numbers[59:98])
    if len(sublist) < 2:
        return None
    return sublist[-2]