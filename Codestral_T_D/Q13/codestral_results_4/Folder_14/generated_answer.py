def find_second_largest_num(numbers):
    sublist = sorted(numbers[5:8], reverse=True)
    return sublist[1] if len(sublist) > 1 else None