def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_largest = None
    largest = None
    for i in range(12, 93):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] < largest and numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest