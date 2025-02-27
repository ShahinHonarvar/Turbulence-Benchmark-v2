def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    start_index = 262
    end_index = 746
    if start_index >= len(numbers) or end_index >= len(numbers) or start_index > end_index:
        return None
    numbers_slice = numbers[start_index:end_index + 1]
    numbers_slice.sort()
    if len(numbers_slice) < 2:
        return None
    return numbers_slice[-2]