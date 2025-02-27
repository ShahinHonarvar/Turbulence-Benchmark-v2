def find_second_smallest_num(numbers):
    if 90 > len(numbers) or 200 < len(numbers):
        return None
    else:
        sublist = numbers[90:201]
        sublist.sort()
        if len(sublist) < 2:
            return None
        elif sublist[1] == sublist[0]:
            return None
        else:
            return sublist[1]