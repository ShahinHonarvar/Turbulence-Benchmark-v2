def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    sliced_numbers = numbers[1:9]
    if len(sliced_numbers) < 2:
        return None
    first_largest = second_largest = float('-inf')
    for num in sliced_numbers:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None