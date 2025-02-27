def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sliced_numbers = numbers[91:100]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    return sliced_numbers[-2]