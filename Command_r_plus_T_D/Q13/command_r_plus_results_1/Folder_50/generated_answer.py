def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 85 or len(set(numbers[70:85])) < 2:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for index in range(70, 85):
        if numbers[index] > largest:
            second_largest = largest
            largest = numbers[index]
        elif numbers[index] > second_largest and numbers[index] != largest:
            second_largest = numbers[index]
    return second_largest