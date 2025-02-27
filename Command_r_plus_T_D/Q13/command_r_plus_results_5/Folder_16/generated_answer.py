def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 37:
        return None
    relevant_numbers = numbers_list[33:37]
    relevant_numbers.sort()
    if len(set(relevant_numbers)) < 2:
        return None
    return relevant_numbers[-2]