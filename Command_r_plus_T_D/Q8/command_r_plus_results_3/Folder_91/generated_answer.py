def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for num in int_list[1:6] if num % 2 == 0]