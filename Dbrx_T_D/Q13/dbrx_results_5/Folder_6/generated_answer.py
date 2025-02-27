def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) < 10:
        return None
    second_largest = None
    largest = None
    for i in range(10, 67):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < largest:
            second_largest = numbers[i]
    if second_largest is None or second_largest < numbers[10] or second_largest > numbers[66]:
        return None
    return second_largest