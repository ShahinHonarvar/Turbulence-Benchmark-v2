def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 8:
        return None
    numbers.sort()
    return numbers[1]