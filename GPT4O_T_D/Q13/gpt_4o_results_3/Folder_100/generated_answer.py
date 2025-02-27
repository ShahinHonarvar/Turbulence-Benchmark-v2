def find_second_largest_num(numbers):
    if len(numbers) < 69:
        return None
    sublist = numbers[42:69]
    if len(sublist) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in sublist:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None