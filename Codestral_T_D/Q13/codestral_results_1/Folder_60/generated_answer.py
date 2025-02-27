def find_second_largest_num(numbers):
    subset = numbers[75:86]
    if len(subset) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in subset:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest