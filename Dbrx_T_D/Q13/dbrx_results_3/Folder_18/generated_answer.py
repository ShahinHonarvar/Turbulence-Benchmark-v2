def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 35:
        return None
    numbers_in_range = numbers[35:50]
    first_largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers_in_range:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None