def find_second_largest_num(numbers):
    if len(numbers) > 6:
        sublist = numbers[6:7]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None