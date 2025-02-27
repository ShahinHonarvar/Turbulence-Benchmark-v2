def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start_index = 59
    end_index = 77
    divisor = -95
    divisible_numbers = [num for num in numbers_list[start_index:end_index + 1] if num % divisor == 0]
    return divisible_numbers