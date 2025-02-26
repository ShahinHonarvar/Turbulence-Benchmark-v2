def all_odd_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return []
    target_element = numbers[23]
    if target_element % 2 == 1:
        return [target_element]
    return []