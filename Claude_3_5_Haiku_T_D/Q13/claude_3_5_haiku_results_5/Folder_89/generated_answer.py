def find_second_largest_num(numbers):
    if len(numbers) <= 56 or not 56 <= 82 < len(numbers):
        return None
    subset = numbers[56:83]
    if len(subset) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None