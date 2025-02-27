def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        sublist = sorted(numbers[3:6], reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]