def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 41:
        return None
    sublist = numbers[40:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]