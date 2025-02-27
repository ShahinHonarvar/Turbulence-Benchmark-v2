def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    relevant_numbers = numbers_list[59:98]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[-2]