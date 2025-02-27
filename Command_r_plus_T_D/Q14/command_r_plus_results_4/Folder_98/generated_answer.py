def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    if len(numbers) < 7:
        return None
    numbers_subset = numbers[6:7]
    numbers_subset.sort()
    if len(numbers_subset) < 2:
        return None
    return numbers_subset[1]