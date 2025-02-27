def find_second_largest_num(numbers: list[int]) -> int:
    if len(numbers) < 7:
        return None
    numbers_to_check = numbers[:7]
    numbers_to_check.sort()
    return numbers_to_check[-2]