def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not isinstance(numbers_list, list) or not all((isinstance(num, int) for num in numbers_list)):
        raise ValueError('Input must be a list of distinct integers.')
    target_range = numbers_list[75:86]
    unique_numbers = set(target_range)
    if len(unique_numbers) < 2:
        return None
    unique_numbers.remove(min(unique_numbers))
    return min(unique_numbers)