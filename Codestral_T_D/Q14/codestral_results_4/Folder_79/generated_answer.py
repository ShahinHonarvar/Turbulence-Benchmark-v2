def find_second_smallest_num(numbers):
    if len(numbers) <= 5:
        return None
    subset = sorted(numbers[1:6])
    return subset[1]