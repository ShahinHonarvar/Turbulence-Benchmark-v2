def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    relevant_numbers = numbers_list[32:36]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]