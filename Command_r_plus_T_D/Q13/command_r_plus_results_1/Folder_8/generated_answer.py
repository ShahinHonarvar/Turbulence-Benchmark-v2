def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 24:
        return None
    else:
        numbers_slice = numbers[23:24]
        return max(numbers_slice)