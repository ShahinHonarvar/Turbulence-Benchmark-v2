def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    target_numbers = numbers_list[33:37]
    target_numbers.sort()
    if len(target_numbers) < 2:
        return None
    return target_numbers[-2]