def find_second_largest_num(numbers):
    if len(numbers) < 58 or not 56 <= len(numbers) - 1:
        return None
    subset = numbers[56:99]
    if len(subset) < 2:
        return None
    largest = max(subset)
    second_largest = float('-inf')
    for num in subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None