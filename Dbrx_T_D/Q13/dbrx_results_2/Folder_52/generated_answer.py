def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_largest = max(numbers[28:38])
    second_largest = float('-inf')
    for num in numbers[28:38]:
        if num < first_largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None