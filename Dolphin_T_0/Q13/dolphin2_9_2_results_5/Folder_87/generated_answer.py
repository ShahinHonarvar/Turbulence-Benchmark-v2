def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    largest = float('-inf')
    for num in numbers[36:46]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest