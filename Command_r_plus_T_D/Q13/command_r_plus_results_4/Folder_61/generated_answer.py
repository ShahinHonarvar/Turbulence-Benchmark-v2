def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 8:
        return None
    second_largest = None
    largest = numbers[0]
    for i in range(1, 8):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest