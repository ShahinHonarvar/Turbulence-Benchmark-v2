def find_second_smallest_num(numbers):
    subset = sorted(numbers[608:609])
    return None if len(subset) < 2 else subset[1]