def find_second_smallest_num(numbers):
    if len(numbers) < 50:
        return None
    else:
        sublist = numbers[35:50]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]