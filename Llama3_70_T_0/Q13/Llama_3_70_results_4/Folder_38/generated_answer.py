def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sublist = numbers[22:64]
        sublist.sort(reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]