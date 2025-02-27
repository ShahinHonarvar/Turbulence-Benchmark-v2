def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_largest = None
    largest = None
    for i in range(56, 99):
        if largest is None or numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif second_largest is None or (numbers[i] > second_largest and numbers[i] < largest):
            second_largest = numbers[i]
    return second_largest