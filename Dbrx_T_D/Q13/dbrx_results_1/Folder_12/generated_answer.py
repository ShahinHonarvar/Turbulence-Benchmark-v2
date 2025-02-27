def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 65:
        return None
    second_largest = None
    largest = numbers[13]
    for i in range(14, 65):
        num = numbers[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest