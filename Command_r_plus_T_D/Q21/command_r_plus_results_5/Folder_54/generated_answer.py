def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_numbers = [num for num in numbers_list[31:73] if num % -63 == 0]
    return divisible_numbers