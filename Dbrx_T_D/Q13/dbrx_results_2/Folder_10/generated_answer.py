def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    second_largest = None
    largest = None
    for i in range(25, 60):
        if numbers[i] > largest or not largest:
            second_largest = largest
            largest = numbers[i]
        elif not second_largest or numbers[i] > second_largest:
            second_largest = numbers[i]
    if second_largest and second_largest != largest:
        return second_largest
    return None