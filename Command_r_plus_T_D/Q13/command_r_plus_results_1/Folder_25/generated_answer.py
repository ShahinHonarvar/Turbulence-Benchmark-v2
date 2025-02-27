def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_largest = None
    largest = float('-inf')
    for i in range(29, 94):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    return second_largest