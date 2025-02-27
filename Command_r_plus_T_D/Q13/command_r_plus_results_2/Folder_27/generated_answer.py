def find_second_largest_num(numbers_list: list[int]) -> int:
    if not isinstance(numbers_list, list) or not all((isinstance(num, int) for num in numbers_list)):
        raise ValueError('Input must be a list of distinct integers.')
    if 66 < len(numbers_list) < 94:
        sub_list = sorted(numbers_list[66:94])
        if len(sub_list) > 1:
            return sub_list[-2]
    return None