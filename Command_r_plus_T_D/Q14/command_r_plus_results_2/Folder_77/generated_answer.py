def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sliced_numbers = numbers[639:976]
    sliced_numbers.sort()
    if len(sliced_numbers) < 2:
        return None
    else:
        return sliced_numbers[1]