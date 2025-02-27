def all_even_ints_exclusive(int_list: list[int]) -> list[int]:
    even_ints = [num for num in int_list[80:200] if num % 2 == 0]
    return even_ints