def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    first_largest = float('-inf')
    second_largest = float('-inf')
    for i in range(200, 201):
        if min_num > numbers[i]:
            min_num = numbers[i]
        if first_largest < numbers[i]:
            second_largest = first_largest
            first_largest = numbers[i]
        elif second_largest < numbers[i] < first_largest:
            second_largest = numbers[i]
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest