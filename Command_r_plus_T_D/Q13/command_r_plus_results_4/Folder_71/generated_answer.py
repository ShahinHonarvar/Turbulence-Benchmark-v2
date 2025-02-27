def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    start_index = 26
    end_index = 52
    if start_index >= len(numbers) or end_index >= len(numbers):
        return None
    sub_list = numbers[start_index:end_index + 1]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]