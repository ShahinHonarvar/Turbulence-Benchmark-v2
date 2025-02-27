def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not isinstance(numbers_list, list) or not all((isinstance(num, int) for num in numbers_list)):
        raise ValueError('Input must be a list of distinct integers.')
    sub_list = sorted(numbers_list[50:55])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]