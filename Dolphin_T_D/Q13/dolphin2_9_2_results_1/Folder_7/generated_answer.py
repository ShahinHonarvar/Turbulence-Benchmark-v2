def find_second_largest_num(numbers):
    if 924 < len(numbers) < 661:
        return None
    sublist = numbers[661:925]
    if len(sublist) < 2:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        return max(sublist)