def find_second_largest_num(numbers):
    sublist = numbers[20:201]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]