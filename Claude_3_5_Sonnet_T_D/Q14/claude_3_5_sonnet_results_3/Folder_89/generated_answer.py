def find_second_smallest_num(numbers):
    sublist = numbers[62:64]
    if len(sublist) < 2:
        return None
    return max(sublist)