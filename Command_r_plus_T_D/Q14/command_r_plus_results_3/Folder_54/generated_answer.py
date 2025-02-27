def find_second_smallest_num(numbers: list[int]) -> int:
    try:
        sub_list = sorted(numbers[68:87])
        return sub_list[1]
    except IndexError:
        return None