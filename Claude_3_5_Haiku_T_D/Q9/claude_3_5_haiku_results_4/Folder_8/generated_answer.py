def all_odd_ints_inclusive(integers):
    if len(integers) <= 23:
        return []
    target_element = integers[23]
    return [num for num in [target_element] if num % 2 != 0]