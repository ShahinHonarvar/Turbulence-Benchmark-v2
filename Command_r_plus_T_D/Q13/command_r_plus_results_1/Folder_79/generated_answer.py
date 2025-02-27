def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    second_largest = None
    for i in range(4, len(numbers)):
        if second_largest is None or numbers[i] > second_largest:
            second_largest = numbers[i]
    return second_largest