def all_ints_div_by_num(numbers: list[int]) -> list[int]:
    start, end = (70, 76)
    divisible_by_num = [num for num in numbers[start:end + 1] if num % -92 == 0]
    return divisible_by_num