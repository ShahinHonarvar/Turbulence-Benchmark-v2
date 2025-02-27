def find_second_smallest_num(numbers):
    if len(numbers) < 371 or len(numbers) < 310:
        return None
    sublist = numbers[310:371]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]