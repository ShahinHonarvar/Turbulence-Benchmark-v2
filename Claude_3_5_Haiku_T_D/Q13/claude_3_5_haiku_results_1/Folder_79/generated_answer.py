def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[4:5]
    if not subset:
        return None
    return subset[0]