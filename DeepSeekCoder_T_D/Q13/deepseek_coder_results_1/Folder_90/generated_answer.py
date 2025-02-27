def find_second_largest_num(numbers):
    if len(numbers) < 747:
        return None
    sublist = numbers[262:747]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]