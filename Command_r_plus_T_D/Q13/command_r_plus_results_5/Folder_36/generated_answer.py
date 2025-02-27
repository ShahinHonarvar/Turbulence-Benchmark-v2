def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 751:
        return None
    numbers_slice = numbers[246:751]
    numbers_slice.sort()
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[-2]