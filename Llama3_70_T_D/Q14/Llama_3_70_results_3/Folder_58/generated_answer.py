def find_second_smallest_num(numbers):
    if len(numbers) < 371:
        return None
    else:
        sublist = sorted(numbers[310:371])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]