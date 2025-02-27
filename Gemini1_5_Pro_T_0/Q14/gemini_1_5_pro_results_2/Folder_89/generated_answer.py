def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[62:64]
    if len(sublist) == 1:
        return None
    elif sublist[0] < sublist[1]:
        return sublist[1]
    else:
        return sublist[0]