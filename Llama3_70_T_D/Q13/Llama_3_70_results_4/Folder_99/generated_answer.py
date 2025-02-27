def find_second_largest_num(numbers):
    slice_ = numbers[310:371]
    if len(slice_) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in slice_:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest