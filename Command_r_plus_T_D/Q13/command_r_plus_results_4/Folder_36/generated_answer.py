def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    start_index = 246
    end_index = 750
    if start_index >= len(numbers) or end_index >= len(numbers):
        return None
    sublist = numbers[start_index:end_index + 1]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[-2]