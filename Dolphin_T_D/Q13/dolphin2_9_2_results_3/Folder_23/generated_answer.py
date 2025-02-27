def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[52:72]
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    second_max = max(sublist)
    return second_max