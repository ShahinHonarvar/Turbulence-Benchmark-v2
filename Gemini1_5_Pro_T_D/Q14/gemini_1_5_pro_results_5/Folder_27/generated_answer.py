def find_second_smallest_num(numbers):
    if len(numbers) < 60:
        return None
    sublist = numbers[25:60]
    min_num = min(sublist)
    sublist.remove(min_num)
    if len(sublist) == 0:
        return None
    return min(sublist)