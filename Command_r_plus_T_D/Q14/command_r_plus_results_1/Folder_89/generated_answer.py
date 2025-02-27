def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[62:64]) < 2:
        return None
    else:
        return sorted(numbers[62:64])[1]