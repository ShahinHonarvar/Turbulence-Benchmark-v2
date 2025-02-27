def find_second_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    sublist = sorted(numbers[15:40])
    if len(sublist) < 2 or sublist[0] == sublist[1]:
        return None
    return sublist[1]