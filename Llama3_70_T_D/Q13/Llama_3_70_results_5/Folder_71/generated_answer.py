def find_second_largest_num(numbers):
    if len(numbers) < 53:
        return None
    sublist = sorted(numbers[26:53], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]