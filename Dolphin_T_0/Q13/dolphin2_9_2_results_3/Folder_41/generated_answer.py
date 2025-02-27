def find_second_largest_num(numbers):
    numbers = numbers[6:7]
    if len(numbers) < 2:
        return None
    largest = second_largest = None
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num
    return second_largest