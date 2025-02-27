def find_second_largest_num(numbers):
    if 63 < len(numbers):
        sublist = sorted(numbers[62:64], reverse=True)
        return sublist[1] if len(sublist) > 1 else None
    return None