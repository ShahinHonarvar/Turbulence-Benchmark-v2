def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[:8]
    sublist.sort()
    return sublist[-2]