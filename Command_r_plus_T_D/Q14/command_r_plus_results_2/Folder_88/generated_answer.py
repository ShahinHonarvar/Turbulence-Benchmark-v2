def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[6:9]) < 2:
        return None
    else:
        numbers_subset = numbers[6:9]
        numbers_subset.sort()
        return numbers_subset[1]