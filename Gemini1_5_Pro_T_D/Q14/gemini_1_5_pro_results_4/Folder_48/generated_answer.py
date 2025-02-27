def find_second_smallest_num(numbers):
    if len(numbers) < 751 or 246 > len(numbers):
        return None
    sublist = numbers[246:751]
    if len(set(sublist)) < 2:
        return None
    temp = sorted(sublist)
    return temp[1]