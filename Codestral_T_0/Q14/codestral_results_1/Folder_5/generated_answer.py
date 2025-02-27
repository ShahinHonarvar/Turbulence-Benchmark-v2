def find_second_smallest_num(numbers):
    if len(numbers) < 6:
        return None
    else:
        sublist = sorted(numbers[3:6])
        return sublist[1] if len(sublist) > 1 else None