def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 49 - 35:
        return None
    first_largest = second_largest = float('-inf')
    for i in range(35, 50):
        if numbers[i] > first_largest:
            second_largest = first_largest
            first_largest = numbers[i]
        elif second_largest < numbers[i] < first_largest:
            second_largest = numbers[i]
    return second_largest if second_largest != float('-inf') else None