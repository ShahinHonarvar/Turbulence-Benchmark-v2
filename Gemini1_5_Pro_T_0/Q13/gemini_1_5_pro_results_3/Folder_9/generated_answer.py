def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers) == 2:
        return min(numbers)
    largest = numbers[0]
    second_largest = numbers[1]
    if second_largest > largest:
        largest, second_largest = (second_largest, largest)
    for i in range(2, len(numbers)):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest