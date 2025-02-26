def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    largest = second_largest = float('-inf')
    for i in range(min(10, len(numbers))):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest if second_largest != float('-inf') else None