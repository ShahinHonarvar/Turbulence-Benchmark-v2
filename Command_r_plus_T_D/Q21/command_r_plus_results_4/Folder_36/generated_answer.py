def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_885 = [num for num in int_list[420:490] if num % 885 == 0]
    return div_by_885