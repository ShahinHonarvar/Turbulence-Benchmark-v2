def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('-inf')
    first_largest = second_largest = min_num
    for num in numbers[246:751]:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest and num < first_largest:
            second_largest = num
    return second_largest if second_largest != min_num else None