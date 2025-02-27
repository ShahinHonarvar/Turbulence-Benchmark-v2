def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    largest = second_largest = float('-inf')
    for i in range(6):
        num = numbers[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None