def find_second_smallest_num(numbers):
    subset = numbers[526:539]
    if len(set(subset)) < 2:
        return None
    else:
        return sorted(subset)[1]