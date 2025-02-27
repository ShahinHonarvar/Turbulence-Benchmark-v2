from typing import List, Generator

def all_ints_div_by_both_two_nums(num_list: List[int]) -> List[int]:
    return [num for num in num_list[42:44] if num % 15 == 0 and num % 87 == 0]