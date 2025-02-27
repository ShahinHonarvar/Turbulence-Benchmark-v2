def find_second_largest_num(numbers):
    if len(numbers) <= 98:
        return None
    sublist = numbers[56:99]
    if len(sublist) < 2:
        return None
    max1 = max(sublist)
    sublist.remove(max1)
    max2 = max(sublist)
    return max2