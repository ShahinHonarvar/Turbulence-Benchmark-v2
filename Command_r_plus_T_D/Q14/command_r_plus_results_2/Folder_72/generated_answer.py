def find_second_smallest_num(numbers: list[int]) -> int:
    try:
        sliced_numbers = sorted(numbers[82:87])
        return sliced_numbers[1]
    except IndexError:
        return None