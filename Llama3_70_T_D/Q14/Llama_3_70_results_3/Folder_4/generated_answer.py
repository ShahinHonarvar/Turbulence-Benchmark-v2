def find_second_smallest_num(numbers):
    if len(numbers) > 84:
        sublist = sorted(numbers[70:85])
        if len(sublist) > 1:
            return sublist[1]
    return None