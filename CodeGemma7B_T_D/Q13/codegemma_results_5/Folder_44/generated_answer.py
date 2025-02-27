def find_second_largest_num(numbers):
    numbers_subset = sorted(numbers[13:69])
    if len(numbers_subset) >= 2:
        return numbers_subset[-2]
    else:
        return None