def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:5]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None