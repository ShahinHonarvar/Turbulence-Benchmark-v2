def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    second_largest = None
    for i in range(19, 93):
        if numbers[i] > numbers[18]:
            if second_largest is None or numbers[i] < second_largest:
                second_largest = numbers[i]
    return second_largest