def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return None
    second_largest = numbers[0] if numbers[0] < numbers[1] else numbers[1]
    largest = numbers[0] if numbers[0] > numbers[1] else numbers[1]
    for num in numbers[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest