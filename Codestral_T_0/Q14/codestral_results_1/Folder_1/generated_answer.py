def find_second_smallest_num(numbers):
    if 34 <= len(numbers) <= 55:
        sublist = sorted(numbers[34:56])
        if len(sublist) > 1:
            return sublist[1]
    return None