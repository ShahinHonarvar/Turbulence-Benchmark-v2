def find_second_smallest_num(numbers):
    sublist = numbers[8:10]
    if len(sublist) < 2:
        return None
    return max(sublist)