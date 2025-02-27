def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    for i in range(34, 56):
        if numbers[i] > numbers[0]:
            second_largest = numbers[i]
            break
    if second_largest is not None:
        for i in range(34, 56):
            if numbers[i] > second_largest and numbers[i] < numbers[0]:
                second_largest = numbers[i]
    if second_largest is None:
        return None
    if second_largest in numbers[56:]:
        return None
    return second_largest