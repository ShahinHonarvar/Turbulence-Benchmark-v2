def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    start_index = 55
    end_index = 98
    if start_index >= len(numbers_list) or end_index >= len(numbers_list):
        return None
    relevant_numbers = numbers_list[start_index:end_index + 1]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]