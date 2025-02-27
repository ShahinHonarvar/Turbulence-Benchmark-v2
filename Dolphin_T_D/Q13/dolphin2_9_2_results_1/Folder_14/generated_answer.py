def find_second_largest_num(numbers):
    subset = numbers[5:8]
    if len(set(subset)) <= 1:
        return None
    else:
        sorted_subset = sorted(set(subset), reverse=True)
        return sorted_subset[1]