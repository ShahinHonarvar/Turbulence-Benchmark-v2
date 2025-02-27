def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sliced_numbers = numbers[25:60]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[1]