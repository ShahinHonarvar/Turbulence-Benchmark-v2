def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    sublist = numbers[62:64]
    if len(sublist) == 1:
        return None
    else:
        min1 = min(sublist)
        sublist.remove(min1)
        return min(sublist)