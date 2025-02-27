def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers[200:]) < 2:
        return None
    else:
        numbers_from_200 = sorted(numbers[200:])
        return numbers_from_200[-2]