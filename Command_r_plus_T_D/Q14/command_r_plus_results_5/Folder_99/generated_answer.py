def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 609:
        return None
    numbers_in_range = numbers[608:609]
    if len(numbers_in_range) < 2:
        return None
    numbers_in_range.sort()
    return numbers_in_range[1]