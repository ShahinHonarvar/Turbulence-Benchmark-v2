def find_second_largest_num(numbers):
    sublist = numbers[75:95]
    if len(sublist) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sublist:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None