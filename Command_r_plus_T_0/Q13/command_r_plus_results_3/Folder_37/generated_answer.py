def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers[1:6]) < 2:
        return None
    else:
        return sorted(numbers[1:6])[1]