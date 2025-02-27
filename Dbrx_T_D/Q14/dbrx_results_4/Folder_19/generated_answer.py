def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) - 1 < 8:
        return None
    min_four_eight = set(numbers[4:9])
    if len(min_four_eight) < 2:
        return None
    sorted_min_four_eight = sorted(list(min_four_eight))
    return sorted_min_four_eight[1]