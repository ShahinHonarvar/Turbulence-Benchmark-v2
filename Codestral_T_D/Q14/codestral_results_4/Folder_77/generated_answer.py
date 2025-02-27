def find_second_smallest_num(numbers):
    if 639 <= len(numbers) <= 975:
        sublist = sorted(numbers[639:976])
        if len(sublist) > 1:
            return sublist[1]
    return None