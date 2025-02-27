def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[533:606]) < 2:
        return None
    numbers_subset = numbers[533:606]
    numbers_subset.sort()
    return numbers_subset[1]