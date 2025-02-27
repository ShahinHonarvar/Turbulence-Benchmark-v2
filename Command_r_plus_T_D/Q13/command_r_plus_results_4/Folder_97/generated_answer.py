def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_numbers = numbers[40:81]
    if len(sub_numbers) < 2:
        return None
    sub_numbers.sort()
    return sub_numbers[-2]