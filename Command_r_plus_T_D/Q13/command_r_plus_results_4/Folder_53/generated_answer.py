def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_numbers = numbers[100:201]
    sub_numbers.sort()
    if len(sub_numbers) < 2:
        return None
    return sub_numbers[-2]