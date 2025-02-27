def find_second_largest_num(numbers):
    if len(numbers) < 91:
        return None
    sublist = numbers[90:91]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]