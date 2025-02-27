def find_second_smallest_num(numbers):
    if 56 <= len(numbers) <= 82:
        sublist = sorted(numbers[56:83])
        if len(sublist) > 1:
            return sublist[1]
    return None