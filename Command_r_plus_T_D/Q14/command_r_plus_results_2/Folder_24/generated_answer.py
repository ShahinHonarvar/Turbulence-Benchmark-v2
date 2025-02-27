def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[23:24]) < 2:
        return None
    numbers_sorted = sorted(numbers[23:24])
    return numbers_sorted[1]