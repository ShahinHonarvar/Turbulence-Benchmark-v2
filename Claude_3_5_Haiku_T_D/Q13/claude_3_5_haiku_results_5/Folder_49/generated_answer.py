def find_second_largest_num(numbers):
    if len(numbers) < 81 or len(numbers) <= 200:
        return None
    subset = numbers[80:201]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    second_largest = None
    for num in subset:
        if num != first_largest:
            if second_largest is None or num > second_largest:
                second_largest = num
    return second_largest