def find_second_largest_num(numbers):
    if len(numbers) < 100:
        return None
    sublist = numbers[91:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]