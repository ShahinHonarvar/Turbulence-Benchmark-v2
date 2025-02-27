def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 80:
        return None
    sub_array = numbers[29:80]
    sub_array.sort()
    if len(sub_array) < 2:
        return None
    return sub_array[-2]