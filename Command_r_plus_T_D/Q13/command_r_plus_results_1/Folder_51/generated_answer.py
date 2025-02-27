def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 9:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(1, 9):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest