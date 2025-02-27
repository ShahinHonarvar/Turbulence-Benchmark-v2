def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 9:
        return None
    else:
        numbers.sort()
        return numbers[1]