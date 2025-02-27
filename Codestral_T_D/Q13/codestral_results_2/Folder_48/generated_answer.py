def find_second_largest_num(numbers):
    if 533 <= len(numbers) <= 605:
        sublist = sorted(numbers[533:606])
        if len(sublist) > 1:
            return sublist[-2]
    return None