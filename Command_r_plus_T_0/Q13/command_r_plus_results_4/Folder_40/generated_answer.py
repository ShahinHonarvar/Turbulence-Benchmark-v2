def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 3:
        return None
    else:
        numbers.sort()
        return numbers[1]