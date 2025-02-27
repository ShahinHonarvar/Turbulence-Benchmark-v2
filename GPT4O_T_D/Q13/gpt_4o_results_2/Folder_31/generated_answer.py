def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    segment = numbers[75:89]
    if len(segment) < 2:
        return None
    largest = second_largest = float('-inf')
    for number in segment:
        if number > largest:
            second_largest = largest
            largest = number
        elif largest > number > second_largest:
            second_largest = number
    return second_largest if second_largest != float('-inf') else None