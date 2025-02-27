def find_second_smallest_num(numbers):
    if 310 <= len(numbers) <= 370:
        sublist = sorted(numbers[310:371])
        if len(sublist) > 1:
            return sublist[1]
    return None