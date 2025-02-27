def find_second_smallest_num(numbers):
    if 30 > len(numbers) - 1 or 87 > len(numbers) - 1:
        return None
    else:
        sublist = sorted(numbers[30:88])
        return sublist[1] if len(sublist) > 1 else None