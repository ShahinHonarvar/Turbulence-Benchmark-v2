def find_second_smallest_num(numbers):
    if len(numbers) < 51 or 50 > len(numbers) - 1:
        return None
    sublist = numbers[22:51]
    min_num = min(sublist)
    sublist.remove(min_num)
    second_min_num = min(sublist)
    return second_min_num