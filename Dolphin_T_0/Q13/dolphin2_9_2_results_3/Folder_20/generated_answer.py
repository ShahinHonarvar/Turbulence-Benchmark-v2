def find_second_largest_num(numbers):
    sublist = numbers[56:67]
    if not sublist:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if not sublist:
        return None
    return max(sublist)