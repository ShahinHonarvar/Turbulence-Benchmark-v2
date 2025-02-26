def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 8:
        subset = numbers[:8]
    else:
        subset = numbers[:8]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = None
    for num in subset:
        if num != largest and (second_largest is None or num > second_largest):
            second_largest = num
    return second_largest