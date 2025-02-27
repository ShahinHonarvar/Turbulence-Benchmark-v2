def find_second_largest_num(numbers):
    if len(numbers) < 56 or len(numbers) < 28:
        return None
    sublist = numbers[27:56]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]