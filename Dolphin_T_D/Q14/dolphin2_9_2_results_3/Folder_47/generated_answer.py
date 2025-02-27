def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    sublist = numbers[22:64]
    sublist = list(set(sublist))
    min_num = min(sublist)
    sublist.remove(min_num)
    if len(sublist) < 1:
        return None
    second_min_num = min(sublist)
    return second_min_num