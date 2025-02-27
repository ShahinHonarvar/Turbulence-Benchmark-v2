def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    start_index = 533
    end_index = 605
    if start_index >= len(numbers_list) or end_index >= len(numbers_list):
        return None
    sub_list = numbers_list[start_index:end_index + 1]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]