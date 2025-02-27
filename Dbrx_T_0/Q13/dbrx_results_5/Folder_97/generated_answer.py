def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 81:
        return None
    second_largest = None
    largest = None
    for i in range(40, 81):
        if numbers[i] > largest or largest is None:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < largest:
            second_largest = numbers[i]
    if second_largest is not None:
        return second_largest
    else:
        return None