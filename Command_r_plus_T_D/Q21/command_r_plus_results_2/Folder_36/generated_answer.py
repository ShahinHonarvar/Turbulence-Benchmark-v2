def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_885 = [num for num in numbers_list[420:490] if num % 885 == 0]
    return divisible_by_885