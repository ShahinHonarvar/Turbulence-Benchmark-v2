def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    result = [num for i, num in enumerate(int_list[255:619], start=255) if num % 965 == 0]
    return result