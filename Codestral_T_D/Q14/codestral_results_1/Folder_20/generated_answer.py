def find_second_smallest_num(numbers):
    subset = sorted(numbers[75:95])
    return None if len(subset) < 2 else subset[1]