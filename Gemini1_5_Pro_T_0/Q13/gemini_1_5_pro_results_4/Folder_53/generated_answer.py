def find_second_largest_num(numbers):
    if len(numbers) < 101:
        return None
    second_largest = None
    largest = numbers[100]
    for i in range(101, 201):
        if i >= len(numbers):
            break
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or (numbers[i] > second_largest and numbers[i] != largest):
            second_largest = numbers[i]
    return second_largest