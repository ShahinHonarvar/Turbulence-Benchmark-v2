def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    second_largest = None
    largest = numbers[4]
    for index in range(5, len(numbers)):
        if numbers[index] > largest:
            second_largest = largest
            largest = numbers[index]
        elif numbers[index] > second_largest and numbers[index] != largest:
            second_largest = numbers[index]
    return second_largest