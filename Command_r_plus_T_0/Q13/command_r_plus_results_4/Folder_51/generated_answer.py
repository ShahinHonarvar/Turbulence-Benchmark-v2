def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 9 or not all((isinstance(num, int) for num in numbers)):
        return None
    second_largest = None
    largest = numbers[0]
    for index in range(1, 9):
        if numbers[index] > largest:
            second_largest = largest
            largest = numbers[index]
        elif numbers[index] > second_largest and numbers[index] != largest:
            second_largest = numbers[index]
    return second_largest