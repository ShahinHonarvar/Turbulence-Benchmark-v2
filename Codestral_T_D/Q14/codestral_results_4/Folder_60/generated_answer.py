def find_second_smallest_num(numbers):
    if 56 <= len(numbers) <= 98:
        sublist = numbers[56:99]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
        else:
            return None
    else:
        return None