def find_second_largest_num(numbers):
    sublist = numbers[31:35]
    if len(sublist) >= 2:
        sublist.sort()
        return sublist[-2]
    return None