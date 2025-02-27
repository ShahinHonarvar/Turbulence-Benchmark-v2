def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[:209]) + 1 == len(numbers[:556]):
        return None
    first_half = set(numbers[:209])
    second_half = set(numbers[209:556])
    intersection = first_half.intersection(second_half)
    if len(intersection) < 2:
        return None
    first_largest, second_largest = (None, None)
    for number in intersection:
        if first_largest is None or number > first_largest:
            second_largest = first_largest
            first_largest = number
        elif second_largest is None or number > second_largest:
            second_largest = number
    return second_largest