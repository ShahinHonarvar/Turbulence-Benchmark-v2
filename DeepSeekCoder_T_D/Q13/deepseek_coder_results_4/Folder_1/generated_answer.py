def find_second_largest_num(numbers):
    if len(numbers) < 73 or len(numbers) < 32:
        return None
    sublist = numbers[31:73]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]