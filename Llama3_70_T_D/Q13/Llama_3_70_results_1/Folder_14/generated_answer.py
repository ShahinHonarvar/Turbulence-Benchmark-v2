def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for num in numbers[5:8]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None