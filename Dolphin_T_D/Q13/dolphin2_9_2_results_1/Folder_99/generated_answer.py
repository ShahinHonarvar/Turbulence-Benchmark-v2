def find_second_largest_num(list_of_numbers):
    subset = list_of_numbers[310:370]
    if len(subset) < 2:
        return None
    else:
        sorted_subset = sorted(set(subset), reverse=True)
        return sorted_subset[1]