def find_second_smallest_num(numbers):
    subset = numbers[10:67]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]