def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    sublist = numbers[20:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]