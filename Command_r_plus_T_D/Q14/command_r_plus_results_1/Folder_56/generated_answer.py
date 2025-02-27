def find_second_smallest_num(numbers_list: list[int]) -> int:
    unique_numbers = set(numbers_list)
    unique_numbers_list = list(unique_numbers)
    unique_numbers_list.sort()
    if len(unique_numbers_list) > 1:
        return unique_numbers_list[1]
    return None