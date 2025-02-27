def find_second_smallest_num(numbers):
    numbers_subset = numbers[50:55]
    numbers_subset.sort()
    if len(numbers_subset) >= 2:
        return numbers_subset[1]
    else:
        return None