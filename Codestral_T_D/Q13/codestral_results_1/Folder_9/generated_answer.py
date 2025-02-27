def find_second_largest_num(numbers):
    if 200 >= len(numbers):
        return None
    else:
        sublist = sorted(numbers[200:201], reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]