def find_second_smallest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        return None
    sorted_numbers = sorted(numbers_list[20:201])
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[1]