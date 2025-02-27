def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 9 or len(set(numbers)) < 9:
        return None
    numbers.sort()
    return numbers[-2]