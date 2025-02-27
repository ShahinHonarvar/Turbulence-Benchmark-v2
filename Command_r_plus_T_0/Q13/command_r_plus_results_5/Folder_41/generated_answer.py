def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 7:
        return None
    else:
        numbers_slice = numbers[6:7]
        return sorted(numbers_slice)[-2] if len(numbers_slice) > 1 else None