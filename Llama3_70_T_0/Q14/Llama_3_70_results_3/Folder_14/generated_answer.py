def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        sublist = numbers[8:10]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]