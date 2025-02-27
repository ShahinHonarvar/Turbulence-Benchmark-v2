def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 609:
        return None
    else:
        numbers_subset = numbers[608:609]
        numbers_subset.sort()
        return numbers_subset[1]