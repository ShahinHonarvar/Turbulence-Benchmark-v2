def find_second_largest_num(numbers):
    if len(numbers) < 64 or 22 >= len(numbers):
        return None
    sublist = numbers[22:64]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]