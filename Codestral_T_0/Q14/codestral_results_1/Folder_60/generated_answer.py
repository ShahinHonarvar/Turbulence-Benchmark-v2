def find_second_smallest_num(numbers):
    if 56 <= len(numbers) <= 98:
        sublist = sorted(numbers[56:99])
        if len(sublist) > 1:
            return sublist[1]
    return None