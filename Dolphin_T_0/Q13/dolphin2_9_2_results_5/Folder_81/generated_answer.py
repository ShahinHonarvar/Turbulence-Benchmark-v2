def find_second_largest_num(numbers):
    numbers_sublist = numbers[10:101]
    numbers_sorted = sorted(set(numbers_sublist), reverse=True)
    if len(numbers_sorted) < 2:
        return None
    else:
        return numbers_sorted[1]