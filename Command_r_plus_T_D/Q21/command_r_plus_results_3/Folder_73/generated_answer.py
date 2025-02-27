def all_ints_div_by_num(lst: list[int]) -> list[int]:
    start_index = 18
    end_index = 38
    divisor = -97
    divisible_numbers = [num for num in lst[start_index:end_index + 1] if num % divisor == 0]
    return divisible_numbers