def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    try:
        sub_list = sorted(numbers[66:94])
        return sub_list[1]
    except IndexError:
        return None