def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 6:
        return None
    second_largest = None
    for index in range(1, 6):
        if second_largest is None or numbers[index] > second_largest:
            second_largest = numbers[index]
    return second_largest