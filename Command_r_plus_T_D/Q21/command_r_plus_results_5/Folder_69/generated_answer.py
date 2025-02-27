def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start, end = (43, 76)
    divisible_by_14 = [num for num in numbers_list[start:end + 1] if num % 14 == 0]
    return divisible_by_14