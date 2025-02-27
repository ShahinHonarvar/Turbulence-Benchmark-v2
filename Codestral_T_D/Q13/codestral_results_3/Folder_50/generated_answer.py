def find_second_largest_num(numbers):
    sublist = numbers[70:85]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return None if second_largest == float('-inf') else second_largest