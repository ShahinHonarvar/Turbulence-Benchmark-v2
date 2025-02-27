def all_ints_div_by_num(lst: list[int]) -> list[int]:
    start_index = 59
    end_index = 78
    divisible_by = -95
    divisible_ints = [num for num in lst[start_index:end_index] if num % divisible_by == 0]
    return divisible_ints