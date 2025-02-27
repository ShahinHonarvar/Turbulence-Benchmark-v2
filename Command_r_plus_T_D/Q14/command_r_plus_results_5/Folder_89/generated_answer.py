def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 64:
        return None
    else:
        numbers_slice = numbers[62:64]
        numbers_slice.sort()
        return numbers_slice[1] if len(numbers_slice) > 1 else None