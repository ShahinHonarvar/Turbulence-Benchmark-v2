def find_second_smallest_num(numbers):
    if len(numbers) < 539:
        return None
    sublist = sorted(numbers[527:539])
    return sublist[1] if len(sublist) > 1 else None