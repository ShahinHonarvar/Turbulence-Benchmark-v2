def find_second_smallest_num(numbers):
    if len(numbers[28:39]) < 2:
        return None
    else:
        sublist = sorted(numbers[28:39])
        return sublist[1]