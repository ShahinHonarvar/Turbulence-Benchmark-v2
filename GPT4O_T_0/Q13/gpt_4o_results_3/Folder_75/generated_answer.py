def find_second_largest_num(numbers):
    if len(numbers) < 58:
        return None
    sublist = numbers[56:58]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]