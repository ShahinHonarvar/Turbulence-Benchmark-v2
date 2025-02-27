def find_second_largest_num(numbers):
    num_range = numbers[56:58]
    if len(num_range) > 0:
        return sorted(num_range)[-2] if len(set(num_range)) > 1 else None