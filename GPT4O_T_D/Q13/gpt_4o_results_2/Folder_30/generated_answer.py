def find_second_largest_num(numbers):
    subarray = numbers[55:99]
    if len(subarray) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in subarray:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None