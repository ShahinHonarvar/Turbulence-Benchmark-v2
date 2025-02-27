def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    largest = max(numbers[1:9])
    second_largest = None
    for i in range(1, 9):
        if numbers[i] != largest and (second_largest is None or numbers[i] > second_largest):
            second_largest = numbers[i]
    return second_largest