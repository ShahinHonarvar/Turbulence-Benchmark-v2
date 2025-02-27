def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sliced_numbers = numbers[55:99]
    if len(sliced_numbers) < 2:
        return None
    sliced_numbers.sort()
    return sliced_numbers[-2]