def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[6:7]) < 2:
        return None
    else:
        numbers_sorted = sorted(numbers[6:7])
        return numbers_sorted[1]