def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[8:10]) < 2:
        return None
    else:
        return sorted(numbers[8:10])[1]