def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    start_index = 75
    end_index = 85
    divisor = -40
    divisible_numbers = [num for num in numbers_list[start_index:end_index + 1] if num % divisor == 0]
    return divisible_numbers