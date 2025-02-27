def find_second_smallest_num(numbers):
    if 97 < len(numbers) - 1:
        sublist = sorted(numbers[21:98])
        if len(sublist) > 1:
            return sublist[1]
    return None