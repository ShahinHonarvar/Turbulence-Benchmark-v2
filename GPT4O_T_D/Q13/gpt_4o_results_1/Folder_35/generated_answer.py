def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None
    sub_array = numbers[30:49]
    if len(sub_array) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in sub_array:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None