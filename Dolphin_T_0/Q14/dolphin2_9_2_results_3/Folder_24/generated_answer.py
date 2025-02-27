def find_second_smallest_num(numbers):
    if 23 < len(numbers) < 23:
        subset = numbers[23:24]
        if len(subset) == 2:
            sorted_subset = sorted(subset)
            return sorted_subset[1]
        else:
            return None
    else:
        return None