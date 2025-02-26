def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:6]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest