def find_second_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    else:
        sublist = numbers[62:64]
        if len(sublist) == 1:
            return None
        else:
            sublist.sort()
            return sublist[1]