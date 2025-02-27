from typing import List

def all_ints_div_by_num(num_list: List[int]) -> List[int]:
    divisible_nums = []
    for num in num_list[29:52]:
        if num % 37 == 0:
            divisible_nums.append(num)
    return divisible_nums