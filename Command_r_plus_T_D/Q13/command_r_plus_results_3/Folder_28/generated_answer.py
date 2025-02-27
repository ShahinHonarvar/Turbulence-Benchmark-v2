def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 64:
        return None
    else:
        numbers_range = numbers[62:64]
        numbers_range.sort()
        return numbers_range[1] if len(numbers_range) > 1 else None