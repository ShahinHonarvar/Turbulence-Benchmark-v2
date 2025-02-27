def find_second_largest_num(numbers):
    if 209 >= len(numbers) or 556 >= len(numbers):
        return None
    sublist = sorted(numbers[209:557], reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]