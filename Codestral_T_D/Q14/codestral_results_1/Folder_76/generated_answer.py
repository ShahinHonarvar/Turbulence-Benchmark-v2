def find_second_smallest_num(numbers):
    if 533 <= len(numbers) <= 605:
        sublist = sorted(numbers[533:606])
        if len(sublist) > 1:
            return sublist[1]
    return None