def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 91:
        return None
    else:
        numbers_slice = numbers[90:91]
        numbers_slice.sort()
        return numbers_slice[1] if len(numbers_slice) > 1 else None