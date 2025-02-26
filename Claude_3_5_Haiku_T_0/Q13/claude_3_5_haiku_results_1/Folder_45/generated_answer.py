def find_second_largest_num(numbers):
    if len(numbers) <= 31 or len(numbers) < 201:
        return None
    subset = numbers[30:201]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = float('-inf')
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None