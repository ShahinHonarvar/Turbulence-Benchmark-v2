def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers[15:40]) < 2:
        return None
    else:
        sliced_numbers = sorted(numbers[15:40])
        return sliced_numbers[1]