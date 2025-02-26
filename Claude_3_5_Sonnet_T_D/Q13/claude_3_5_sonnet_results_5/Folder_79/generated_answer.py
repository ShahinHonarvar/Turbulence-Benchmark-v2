def find_second_largest_num(numbers):
    if len(numbers) <= 4:
        return None
    subset = numbers[4:5]
    if len(subset) == 0:
        return None
    elif len(subset) == 1:
        return subset[0]
    else:
        return None