def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_largest = float('-inf')
    largest = float('-inf')
    for i in range(15, 52):
        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] != largest:
            second_largest = numbers[i]
    if second_largest == float('-inf'):
        return None
    else:
        return second_largest