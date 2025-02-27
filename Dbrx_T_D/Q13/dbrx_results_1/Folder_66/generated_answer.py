def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('-inf')
    first_largest = second_largest = min_num
    for num in numbers[50:55]:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != min_num else None