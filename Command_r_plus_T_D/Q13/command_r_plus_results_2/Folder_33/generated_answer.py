def find_second_largest_num(numbers_list: list[int]) -> int:
    if not isinstance(numbers_list, list) or not all((isinstance(num, int) for num in numbers_list)):
        raise ValueError('Input must be a list of distinct integers.')
    if len(numbers_list) < 775:
        return None
    relevant_numbers = numbers_list[667:775]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]