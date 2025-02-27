def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers[64:67]) < 2:
        return None
    else:
        return sorted(numbers[64:67])[-2]