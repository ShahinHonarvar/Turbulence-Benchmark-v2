def find_second_largest_num(numbers):
    subset = numbers[25:88]
    if len(subset) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest