def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    subset = numbers[6:7]
    if not subset:
        return None
    return subset[0]