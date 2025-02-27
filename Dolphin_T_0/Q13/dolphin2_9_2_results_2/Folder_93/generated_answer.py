def find_second_largest_num(numbers):
    subset = numbers[75:95]
    if len(subset) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest