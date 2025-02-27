def find_second_largest_num(numbers):
    if len(numbers) < 86:
        return None
    numbers = numbers[75:86]
    largest = second_largest = float('-inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None