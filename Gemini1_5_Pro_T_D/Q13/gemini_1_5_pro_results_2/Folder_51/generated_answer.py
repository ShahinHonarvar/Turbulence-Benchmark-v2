def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[1:9]) < 2:
        return None
    largest = numbers[1]
    second_largest = numbers[2]
    if second_largest > largest:
        largest, second_largest = (second_largest, largest)
    for i in range(3, 9):
        if i > len(numbers) - 1:
            break
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest