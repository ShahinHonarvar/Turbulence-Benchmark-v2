def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    subset = numbers[10:11]
    if not subset:
        return None
    return subset[0]