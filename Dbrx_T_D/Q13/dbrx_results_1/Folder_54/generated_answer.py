def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    first_largest = second_largest = float('-inf')
    for num in numbers[34:56]:
        if num <= min_num:
            continue
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None