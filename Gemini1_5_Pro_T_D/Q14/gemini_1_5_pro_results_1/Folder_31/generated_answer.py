def find_second_smallest_num(numbers):
    if len(numbers) < 94 or len(numbers) < 30:
        return None
    else:
        sublist = numbers[29:94]
        if len(set(sublist)) < 2:
            return None
        else:
            sublist.sort()
            return sublist[1]