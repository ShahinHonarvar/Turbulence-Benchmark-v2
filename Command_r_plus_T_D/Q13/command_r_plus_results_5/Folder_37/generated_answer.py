def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 6:
        return None
    second_largest = None
    for i in range(1, 6):
        if second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest