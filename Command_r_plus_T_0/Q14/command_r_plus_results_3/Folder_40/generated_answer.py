def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 3:
        return None
    numbers.sort()
    return numbers[1]